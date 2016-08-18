Cities
======

Base of Countries and Cities around the world. Sources used from:

* Geonames: http://www.geonames.org/countries/
* Maxmind: https://www.maxmind.com/pt/free-world-cities-database

Country
=======

The source file of countries is named as `countries.txt`. This file presents
data separated by a `tab` char, these are the columns available:

* __iso__: ISO
* __iso3__: ISO3
* __iso_numeric__: ISO-Numeric
* __fips__: fips
* __country__: Country
* __capital__: Capital
* __area__: Area(in sq km)
* __population__: Population
* __continent__: Continent
* __tld__: tld
* __currency_code__: CurrencyCode
* __currency_name__: CurrencyName
* __phone__: Phone
* __postal_code_format__: Postal Code Format
* __postal_code_regex__: Postal Code Regex
* __languages__: Languages
* __geonameid__: geonameid
* __neighbours__: neighbours
* __equivalent_fips_code__: EquivalentFipsCode

Cities
=======

The source file of cities is named as `cities.txt`. This file presents data
separated by a `tab` char, these are the columns available:

* geonameid         : integer id of record in geonames database
* name              : name of geographical point (utf8) varchar(200)
* asciiname         : name of geographical point in plain ascii characters, varchar(200)
* alternatenames    : alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
* latitude          : latitude in decimal degrees (wgs84)
* longitude         : longitude in decimal degrees (wgs84)
* feature class     : see http://www.geonames.org/export/codes.html, char(1)
* feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
* country code      : ISO-3166 2-letter country code, 2 characters
* cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
* admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
* admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80)
* admin3 code       : code for third level administrative division, varchar(20)
* admin4 code       : code for fourth level administrative division, varchar(20)
* population        : bigint (8 byte int)
* elevation         : in meters, integer
* dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
* timezone          : the timezone id (see file timeZone.txt) varchar(40)
* modification date : date of last modification in yyyy-MM-dd format
