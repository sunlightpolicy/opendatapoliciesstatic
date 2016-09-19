#!/usr/bin/python

from bs4 import BeautifulSoup, Comment
from jinja2 import Environment, FileSystemLoader
import os
import glob2

# Make everything utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

files = glob2.glob('./data/**/*.xml')

for current_file in files:

    base_file = os.path.splitext(os.path.basename(current_file))[0]
    new_file = './_documents/{}.md'.format(base_file)

    soup = BeautifulSoup(open(current_file), 'xml')

    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()

    law = {
       'catch_line': soup.law.catch_line.get_text(),
       'text': "".join(str(item) for item in soup.law.find('text').contents).strip(),
       'section_number': soup.law.section_number.get_text(),
       'history': '',
       'structure': [{'label': s['label'], 'identifier': s['identifier'], 'text': s.get_text()} for s in soup.law.structure.find_all('unit')],
       'permalink': ''
    }

    if soup.law.history:
        law['history'] = "".join(str(item) for item in soup.law.history.contents).strip(),

    for structure in law['structure']:
        law['permalink'] += '/' + structure['identifier']
    law['permalink'] += '/' + law['section_number'] + '/'

    env = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)
    new_content = env.get_template('templates/template.md').render(law)

    with open(new_file, 'w') as f:
        f.write(new_content)
