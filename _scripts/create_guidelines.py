from collections import OrderedDict
import bs4
import re
# import sys
import yaml

# sys.setrecursionlimit(100000)

with open('../_data/guideline_details.html', 'r') as guide_file:
    guide_file_contents = guide_file.read()
    GUIDELINES = guide_file_contents.decode('utf-8')

with open('../_data/guideline_examples.html', 'r') as ex_file:
    ex_file_contents = ex_file.read()
    EXAMPLES = ex_file_contents.decode('utf-8')

def read_all(guidelines=GUIDELINES):
    """Side effect: saves a YAML data file with section IDs and names"""

    soup = bs4.BeautifulSoup(guidelines, 'html.parser')
    sections = []
    for li in soup.ul.contents:
        if li.name == 'li':
            sections.append(read_section(li))

    with open('../_data/guideline-sections.yaml', 'w') as outfile:
        for section in sections:
            outfile.write(section[0] + ': ' + section[1] + '\n')
            # outfile.write(yaml.dump(section), default_flow_style=False)

    return

def read_section(li):

    section_id = li.get('id').replace('section-', '')
    name = li.h3.string

    for i in li.find('ol', class_='doc-items').contents:
        if i.name == 'li':
            read_guideline(i, section_id)

    return (section_id, name)

def read_guideline(li, section_id):
    """Side effect: saves a file in _guidelines with this info"""

    # Strip out newlines
    # print str(li)
    # print li
    # print str(li).decode('utf-8')
    contents = re.sub(u'\n *', u'', unicode(li))
    # contents = li.replace('\n', '')
    # print contents

    # Parse the guideline to extract its info
    results = re.search(
        '<li .+><h4><a href="#(.+)">(\d{1,2}) (.+)<\/a><\/h4><p><a.+s<\/a><\/p>(.+)<\/li>',
        contents)
    # print results

    # Get the links to narrative explanations
    examples = read_examples(results.group(1))

    # Format info for guideline file
    # metadata = OrderedDict({
    #     'id': results.group(1),
    #     'number': results.group(2),
    #     'name': results.group(3),
    #     'section': section_id,
    #     'examples': examples
    # })
    # text = results.group(4).replace('</p><p>', '</p>\n<p>')
    metadata = {
        'id': results.group(1),
        'number': results.group(2),
        'name': results.group(3),
        'section': section_id,
        'examples': examples,
        'text': results.group(4).replace('</p><p>', '</p>\n<p>')
    }
    # output = u"""---
    # id: {id}
    # number: {number}
    # name: {name}
    # section: {section}
    # examples: {examples}
    # ---

    # {text}
    # """.format(**metadata)
    output = (u'---\nid: {id}\nnumber: {number}\nname: {name}\n' \
        u'section: {section}\nexamples: {examples}\n---\n\n{text}'.format(**metadata))

    # print text.encode('utf-8')
    # print type(text)
    # print text
    # print [i[1] for i in metadata.items()]
    # print [(i[0] + ': ' + i[1]) for i in metadata.items()]
    # print '\n'.join([(i[0] + ': ' + i[1]) for i in metadata.items()])
    # print type('\n'.join([(i[0] + ': ' + i[1]) for i in metadata.items()]))

    filename = metadata['number'].zfill(2) + '-' + metadata['id'] + '.md'
    with open('../_guidelines/' + filename, 'w') as outfile:
        outfile.write(output.encode('utf-8'))
        # print (u'---\n' +
        #     u'\n'.join([(i[0] + ': ' + i[1]) for i in metadata.items()]) +
        #     u'\n---\n\n' + text)
        # outfile.write(u'---\n' +
        #     u'\n'.join([(i[0] + u': ' + i[1]) for i in metadata.items()]) +
        #     u'\n---\n\n' + text.encode('ascii'))
        # outfile.write('---\n' +
        #     yaml.dump(metadata, default_flow_style=False) +
        #     '---\n\n' + text)

    return

def read_examples(guideline_id, html_doc=EXAMPLES):

    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    this_example = soup.find('li', id=guideline_id)

    # examples_list = []
    examples_list = ''
    if this_example.find('ul', class_='bulleted'):
        for link in this_example.find('ul', class_='bulleted').find_all('a'):
            # examples_list.append({
            #     'url': link.get('href'),
            #     'text': link.string
            # })
            examples_list += ('\n  - url: ' + link.get('href') +
                '\n    title: ' + link.string)

    return examples_list


if __name__ == '__main__':
    
    read_all()
