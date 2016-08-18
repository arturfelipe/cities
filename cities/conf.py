# coding: utf-8
import os

SOURCES_DIR = 'city_sources'

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
        'url': 'http://download.geonames.org/export/dump/cities15000.zip',
        'file_name': 'cities15000.txt',
        'colummns': (
            'geonameid',
            'name',
            'asciiname',
            'alternate_names',
            'latitude',
            'longitude',
            'feature_class',
            'feature_code',
            'country_code',
            'cc2',
            'admin1_code',
            'admin2_code',
            'admin3_code',
            'admin4_code',
            'population',
            'elevation',
            'dem',
            'timezone',
            'modification_date',
        )
    }
}
