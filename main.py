import csv
import requests

FILENAME = 'in.txt'
GEONAMES_USERNAME = 'demo'
LANG = 'ru'
SKIP = ['Where     ', '----------']

with open(FILENAME, 'r', newline='') as incsvfile:
    with open(LANG + '_' + FILENAME, 'w', newline='') as outcsvfile:
        osmweeklyreader = csv.reader(incsvfile, delimiter='|')
        osmweeklywriter = csv.writer(outcsvfile, delimiter='|')
        for row in osmweeklyreader:
            if row [1] not in SKIP:
                r = requests.get('http://api.geonames.org/searchJSON?q=' + row [1] + '&lang=' + LANG + '&username=' + GEONAMES_USERNAME)
                pew = r.json().get('geonames')[0].get('name')
                row [1] = pew
            print (row [1])
            osmweeklywriter.writerow(row)
