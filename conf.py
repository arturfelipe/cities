# coding: utf-8
import os

SOURCES_DIR = 'sources'

SOURCES = {
    'countries': {
        'path': os.path.join(SOURCES_DIR, 'countries.txt'),
        'url': 'http://download.geonames.org/export/dump/countryInfo.txt',
        'exclude_lines_regex': r'^#',
        'colummns': (
            'iso',
            'iso3',
            'iso_numeric',
            'fips',
            'country',
            'capital',
            'area',
            'population',
            'continent',
            'tld',
            'currency_code',
            'currency_name',
            'phone',
            'postal_code_format',
            'postal_code_regex',
            'languages',
            'geonameid',
            'neighbours',
            'equivalent_fips_code',
        )
    },
    'cities': {
        'path': os.path.join(SOURCES_DIR, 'cities.txt'),
    }
}
