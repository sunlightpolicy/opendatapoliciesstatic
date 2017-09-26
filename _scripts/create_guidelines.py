import bs4
import re


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

    # Maybe should have stuck with BeautifulSoup, but whatever, it works

    # Strip out newlines
    contents = re.sub(u'\n *', u'', unicode(li))

    # Parse the guideline to extract its info
    results = re.search(
        '<li .+><h4><a href="#(.+)">(\d{1,2}) (.+)<\/a><\/h4><p><a.+s<\/a><\/p>(.+)<\/li>',
        contents)

    # Get the links to narrative explanations
    examples = read_examples(results.group(1))

    # Format info for guideline file
    metadata = {
        'id': results.group(1),
        'number': results.group(2),
        'name': results.group(3),
        'section': section_id,
        'examples': examples,
        'text': results.group(4).replace('</p><p>', '</p>\n<p>')
    }
    output = (u'---\nid: {id}\nnumber: {number}\nname: {name}\n' \
        u'section: {section}\nexamples: {examples}\n---\n\n{text}'.format(**metadata))

    # Export
    filename = metadata['number'].zfill(2) + '-' + metadata['id'] + '.md'
    with open('../_guidelines/' + filename, 'w') as outfile:
        outfile.write(output.encode('utf-8'))

    return

def read_examples(guideline_id, html_doc=EXAMPLES):

    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    this_example = soup.find('li', id=guideline_id)

    examples_list = ''
    if this_example.find('ul', class_='bulleted'):
        for link in this_example.find('ul', class_='bulleted').find_all('a'):
            examples_list += ('\n  - url: ' + link.get('href') +
                '\n    title: >-\n      ' + link.string)

    return examples_list


if __name__ == '__main__':
    
    read_all()
