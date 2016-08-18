# coding: utf-8
import os
import requests
from conf import SOURCES


def download_source(source_name):
    resp = requests.get(SOURCES[source_name]['url'])
    if resp.status_code == 200:
        with open(SOURCES[source_name]['path'], 'w') as fd:
            fd.write(resp.text)


def check_source(source_name):
    dir_path = os.path.dirname(SOURCES[source_name]['path'])
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
        except OSError as e:
            msg = 'Could not create dir "{}". {}'
            raise Exception(msg.format(dir_path, e))

    if not os.path.exists(SOURCES[source_name]['path']):
        download_source(source_name)


def load_countries():
    lines = []

    with open(SOURCES['countries']['path']) as fd:
        lines = fd.readlines()

    for line in lines:
        data = line.strip('\n').split('\t')
        yield dict(zip(SOURCES['countries']['colummns'], data))


if __name__ == '__main__':
    # countries = list(load_countries())
    # print(list(countries)[0])
    # print(list(countries))
    check_source('countries')
