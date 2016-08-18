# coding: utf-8
import os
import re
import io
import requests
import zipfile
from .conf import SOURCES, SOURCES_DIR


def download_source(source_name):
    url = SOURCES[source_name]['url']
    resp = requests.get(url)

    if resp.status_code == 200:
        source_path = SOURCES[source_name]['path']
        source_content = resp.text

        if url.endswith('.zip'):
            z = zipfile.ZipFile(io.BytesIO(resp.content))
            z_path = z.extract(SOURCES[source_name]['file_name'], SOURCES_DIR)
            os.rename(z_path, source_path)
            return

        with open(source_path, 'w') as fd:
            fd.write(source_content)


def check_source(source_name):
    dir_path = os.path.dirname(SOURCES[source_name]['path'])
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
        except OSError as e:
            msg = 'Could not create dir "{}". {}'
            raise Exception(msg.format(dir_path, e))

    source_path = SOURCES[source_name]['path']
    if not os.path.exists(source_path):
        download_source(source_name)


def load_countries():
    lines = []

    check_source('countries')

    with open(SOURCES['countries']['path']) as fd:
        lines = fd.readlines()

    for line in lines:
        exclude_pattern = SOURCES['countries'].get('exclude_lines_regex')
        if exclude_pattern:
            if re.match(exclude_pattern, line):
                continue

        data = line.strip('\n').split('\t')
        yield dict(zip(SOURCES['countries']['colummns'], data))


def load_cities():
    lines = []

    check_source('cities')

    source_path = SOURCES['cities']['path']
    with open(source_path) as fd:
        lines = fd.readlines()

    for line in lines:
        exclude_pattern = SOURCES['cities'].get('exclude_lines_regex')
        if exclude_pattern:
            if re.match(exclude_pattern, line):
                continue

        data = line.strip('\n').split('\t')
        yield dict(zip(SOURCES['cities']['colummns'], data))


if __name__ == '__main__':
    countries = list(load_countries())
    print(countries[0])
    print(len(countries))

    cities = list(load_cities())
    print(cities[0])
    print(len(cities))
