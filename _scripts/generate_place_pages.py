import geocoder
import os
import re
import time


for doc in os.listdir('../_documents'):
    time.sleep(0.001)  # Time delay to keep geocoding rate within quota
    with open('../_documents/' + doc, 'r') as infile:
        text = infile.read()
        loc = re.search(r'(?<=title: ).+?(?=\()', text).group()
        try:
            city, state = [i.strip() for i in loc.split(',')]
        except ValueError:
            print 'Error when grabbing city, state from ' + doc
        else:
            place = city.lower().replace(' ', '-') + '-' + state.lower()
            try:
                y, x = geocoder.google(loc).latlng
            except ValueError:
                print 'Error geocoding ' + doc
                y, x = '', ''
            with open('../_places/' + place + '.md', 'w') as outfile:
                outfile.write('---' +
                    '\nplace: ' + place +
                    '\ntitle: ' + city +
                    '\nstates:\n  - ' + state.upper() +
                    '\ntype: local' +
                    '\nx: ' + str(x) +
                    '\ny: ' + str(y) +
                    '\n---')

            # place
            # title
            # # name_full
            # states
            # type: local
            # x
            # y
            # # wwc
