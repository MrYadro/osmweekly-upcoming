import csv
import requests

FILENAME = 'in.txt'
GEONAMES_USERNAME = 'Demo'
LANG = 'ru'

with open(FILENAME, 'r', newline='') as incsvfile:
    with open(LANG + '_' + FILENAME, 'w', newline='') as outcsvfile:
        osmweeklyreader = csv.reader(incsvfile, delimiter='|')
        osmweeklywriter = csv.writer(outcsvfile, delimiter='|')
        rownum = 0
        for row in osmweeklyreader:
            if row [1] and rownum > 1:
                r = requests.get('http://api.geonames.org/searchJSON?q=' + row [1] + '&lang=' + LANG + '&username=' + GEONAMES_USERNAME)
                pew = r.json().get('geonames')[0].get('name')
                row [1] = pew
            print (row [1])
            osmweeklywriter.writerow(row)
            rownum += 1
