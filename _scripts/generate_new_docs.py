import os
import re
import urllib2


def make_get_function(doc, text):

    def get(regex):

        try:
            result = re.search(regex, text).group()
        except AttributeError:
            print('Search error in ' + doc + ': ' + regex)
            return ''
        else:
            return result

    return get

def validate_url(url):

    try:
        urllib2.urlopen(url).getcode()
    except (urllib2.URLError, urllib2.socket.error):
        print('This URL may not work: ' + url)
    return

for doc in os.listdir('../_documents/old/'):
    # if ('20' not in doc) and (doc != '.DS_Store'):  # If it's one of the old doc files
        with open('../_documents/old/' + doc, 'r') as infile:
            text = infile.read()
            get = make_get_function(doc, text)
            loc = get(r'(?<=title: ).+?(?=\()')
            try:
                city, state = [i.strip() for i in loc.split(',')]
            except ValueError:
                print 'Error when grabbing city, state from ' + doc
            else:
                place = city.lower().replace(' ', '-') + '-' + state.lower()
                year = get(r'\d{4}(?=.+?Link)')
                legal_custom = get(r'(?<=Means:( |\n)).+?(?=\',)')
                policy_url = get(r'(?<=Link: ).+?(?=;.+?Means:)')
                validate_url(policy_url)
                content = re.search(r'(?<=\n---\n).+', text, re.DOTALL).group()
                with open('../_documents/' + place + '-' + year + '.md',
                    'w') as outfile:
                    outfile.write('---' +
                        '\nplace: ' + place +
                        '\nyear: ' + year +
                        '\nlegal_custom: ' + legal_custom +
                        '\npolicy_url: ' + policy_url +
                        '\n---\n' + content + '\n')
