# coding: utf-8
import os

SOURCES_DIR = 'sources'

CITIES_SOURCE_PATH = os.path.join(SOURCES_DIR, 'cities.txt')
COUNTRIES_SOURCE_PATH = os.path.join(SOURCES_DIR, 'countries.txt')

CITIES_COLUMNS = (
    'iso',
    'iso3',
    'iso_numeric',
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
