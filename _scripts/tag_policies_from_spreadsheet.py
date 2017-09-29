import difflib
import gfm
import os
import pandas as pd
import re
import regex
import us
import yaml

# # pd.read_csv
# # actually read excel

# def try_to_match(input_str, reference_str):
#     """Will test an exact match, then an exact match with quotation marks
#     removed, then a close match (no more than 4 characters off), then
#     a match within quotation marks (like if there's explanatory text)."""

#     if input_str in reference_str:
#         return true
#     elif input_str.strip('"') in reference_str:
#         return true
#     elif regex.search(r'(?:' + regex.escape(input_str) + r'){e<=4}', reference_str):
#         return true
# # add something where you try stripping out HTML?



# Notes:

# Need to convert 'n/a' to no
# Convert blank to unknown... or no?
# Use Joyce/Wenjia notes to compare

# Do something special if contains 'close fit'

# Need to figure out how to deal with HTML
# Multiparagraph? Maybe have a tiered system:
#     Convert to HTML (if Markdown)
#     If quote in text, then tag it
#     If quote not in text, then go paragraph by paragraph, and check for overlap against the quote

# Need a special tag for opposite/negative answers

# Someday need a function to check which guidelines a policy meets



# for block in text:
#     convert to plain text?
#     check for a common substring with spreadsheet cell
#     if common substring:
#         tag the whole block
#         # handle complicated situations


def find_place(converted_name):

    return


def convert_place_name(raw_name):

    # TODO: strip off '.\d' and figure out WHICH policy
    name = re.sub(r'\.\d', '', raw_name.strip())
    if ',' in name:
        parts = re.search(
            r'(.+?)((( and )|-|/)\w+ County)?, ([A-Z])\.?([A-Z])\.?', name)
        return (parts.group(1).lower().replace(' ', '-') + '-' +
            parts.group(5).lower() + parts.group(6).lower())
    else:
        # print unicode(name)
        return us.states.lookup(unicode(name)).abbr.lower()

def is_def_or_guide_col(name):

    return (is_def_col(name) or is_guideline_col(name))

def is_def_col(name):

    return re.search(r'^".+"', name)

def is_guideline_col(name):

    return re.search(r'^\d{1,2}\.', name)

    # if re.search(r'^\d{1,2}\.', column_name____):
    #     num = int(re.search(r'(?<=^)(\d{1,2})(?=\.)', column_name____))

def get_guideline_num(title):

    return title.split('. ')[0]

# loop through all attributes to see if they are guidelines, and if so, check them out

# need definitions for Data, Public Data/Information, Open Data


# r'(<.+>)*_____(<.+>)*'

# html = gfm.markdown(content)



# NEW!!!!!!!
# for line in file:
#     get_matches(orig_text, compare_text)



# MD -> HTML
# For each element:
# for each p, heading, li:
#     look for matches

# Go from beginning to end, stripping out HTML, and adding those tags to a dict that knows the beginning character position
# Compare strings and get matches

# deal with 'Does the opposite' and 'close fit'



# def do_an_entire_doc__all_questions(___):

#     # with file open

#     text_list = ___.split('\n')
#     # do stuff


#     return

# Create a list of guidelines
# Note: index numbers will be 1 less than the guideline numbers
folder = os.path.join('..', '_guidelines')
GUIDELINES = []
for doc in os.listdir(folder):
    # print doc
    if doc[-3:] == '.md':
        with open(os.path.join(folder, doc), 'r') as infile:
            contents = infile.read().decode('utf-8')
            fontmatter = re.search(
                r'(?<=---\n).+(?=\n---\n)', contents, re.DOTALL).group(0)
            GUIDELINES.append(yaml.load(fontmatter))

            #(?<=---\n)(.+)(?=---\n)

# for file in ()
#     with open('../_data/guideline_details.html', 'r') as guide_file:
#         guide_file_contents = guide_file.read()
#         GUIDELINES = guide_file_contents.decode('utf-8')


DEFINITIONS = {
  'data': 'Data',
  'public': 'Public Data/Information',
  'open': 'Open Data'
}


# look through spreadsheet:
# for each entry, look at city + year to try to figure out which policy it corresponds with
    # if no match, print warning
    # if miltiple matches, print warning and don't do anything
    # if one match, proceed


def run_all_docs():

    folder = '../_documents/'
    sheet = load_comparison_sheet()
    for index, row in sheet.iterrows():
        matching_docs = ([filename for filename in os.listdir(folder)
            if filename.startswith(index)])
        if len(matching_docs) == 0:
            print("No matching policies found for " + index +
                ". Ignored from tagging.")
        elif len(matching_docs) > 1:
            print("Multiple matching policies found for " + index +
                ". Ignored from tagging.")
        else:
            # blah
            in_file = open(folder + matching_docs[0], 'r')
            in_text = in_file.read().decode('utf-8')
            in_file.close()
            if re.search('no_text: true', in_text):
                print('\nNo text for ' + matching_docs[0] +
                    '. Ignored from tagging.')
            else:
                parts = re.search(r'(^---.+\n---\n)(.+)', in_text,
                    re.M|re.DOTALL)
                tagged_text = run_one_doc(parts.group(2), row)
                out_file = open(folder + matching_docs[0],'w')
                out_file.write((parts.group(1) + tagged_text).encode('utf-8'))
                out_file.close()
            # with open(folder + matching_docs[0], 'r+') as file:
            #     in_text = file.read().decode('utf-8')
            #     # out_text = re.sub(r'(?<=^---.+\n---\n)(.+)',
            #     #     run_one_doc(r'\1', row), in_text, re.M|re.DOTALL)
            #     # file.truncate()
            #     # file.write(out_text)
            #     parts = re.search(r'(^---.+\n---\n)(.+)', in_text,
            #         re.M|re.DOTALL)
            #     file.truncate()
            #     try:
            #         tagged_text = run_one_doc(parts.group(2), row)
            #     except AttributeError:
            #         print parts
            #         print parts.group(0)
            #         file.write(in_text)
            #     else:
            #         file.write((parts.group(1) + tagged_text).encode('utf-8'))

    return sheet

def load_comparison_sheet(
    filename='../_data/Open Data Policy Comparison- Best Practices.xlsx'):

    raw = pd.read_excel(filename).drop(pd.np.NaN).transpose()
    # print full_sheet.index.map(convert_place_name)
    # print full_sheet['Year Enacted']

    # Drop rows that aren't actual policies
    raw.drop(raw.index[raw.index.str.startswith('# ')], inplace=True)
    raw.drop(raw.index[raw.index.str.startswith('Unnamed:')], inplace=True)
    raw.drop(raw.index[raw.index.str.startswith('percentage')], inplace=True)

    # Create place-year attribute, to be used to matching with policy files
    raw['place-year'] = raw.apply(
        lambda row: convert_place_name(row.name) + '-' +
        str(row['Year Enacted']), axis=1)
    # raw['place-year'] = (raw.index.map(convert_place_name) +
    #     '-' + str(raw['Year Enacted']))

    # Drop cases where multiple polices for place for one year (temporary!)
    py_value_counts = raw['place-year'].value_counts()
    for place_year in py_value_counts[py_value_counts > 1].index.tolist():
        print("Multiple " + place_year + " entries found. Ignored from tagging.")
    raw.drop_duplicates(subset='place-year', keep=False, inplace=True)

    # Set place-year as the new index
    raw.set_index('place-year', inplace=True)

    # Drop columns that we don't need
    keep_cols = [col for col in raw.columns if is_def_or_guide_col(col)]
    sheet = raw[keep_cols]

    return sheet


def run_one_doc(text, responses):

    def print_warning(warning, for_what):

        if warning:
            print(warning + ' for ' + for_what)

        return

    # def get_response(question):

    #     return responses[question]

    print('\nRunning: ' + responses.name)

    for def_code in DEFINITIONS:
        response = responses['"' + DEFINITIONS[def_code] + '"']
        if response in ['', 'n/a']:
            pass
        else:
            gt = get_and_tag(
                text, response, 'def-' + def_code)
            text = gt['text']
            print_warning(gt['warning'], DEFINITIONS[def_code])
    for guideline in GUIDELINES:
        g_title = responses.index.str.startswith(str(guideline['number']) + '.')
        response = responses[g_title][0]
        if response in ['', 'n/a']:
            pass
        else:
            gt = get_and_tag(
                text, response, 'g-' + guideline['id'])
            text = gt['text']
            print_warning(gt['warning'], 'guideline ' + str(guideline['number']))

    return text

def get_and_tag(orig_text, compare_text, tag):
    """Go through a doc looking for matches for a single definition,
    then tags them as such."""

    # Converts newlines to long string of '@#~'s, so tagged spans will never
    # contain multiple paragraphs/list items.

    if compare_text in ['n/a', 'N/A', pd.np.NaN]:

        return {
            'text': orig_text,
            'warning': None
        }

    else:

        new_text = orig_text.replace('\n', '@#~'*10)
        matches = get_matches(new_text, compare_text)
        if len(matches['output_list']) == 0:
            warning = 'No matches were found'
        elif matches['no_match_length'] >= 45:
            warning = str(matches['no_match_length']) + ' characters didn\'t match'
        else:
            warning = None
        new_text = tag_all_matches(new_text, matches['output_list'], tag)
        # new_text_list = orig_text_list[:]
        # for x in range(len(new_text_list)):
        #     line_matches = get_matches(new_text_list[x], compare_text)
        #     new_text_list[x] = tag_all_matches(new_text_list[x], line_matches, tag)
            # for match in line_matches:
            #     line_w_end_tag = insert_html(</, line, match[1])
            #     line_w_both_tags = insert_html(, match[0])
            # line = line_w_both_tags

        # Convert our long char strings back to newline characters
        new_text = new_text.replace('@#~'*10, '\n')

        # return new_text_list
        return {
            'text': new_text,
            'warning': warning
        }

def tag_all_matches(text_line, matches, tag):

    new_text_line = text_line
    # list sorted in reverse order so that HTML is inserted from right to left,
    # so that insertion doesn't mess up character position numbers
    for match in sorted(matches, reverse=True):
        new_text_line = tag_single_match(new_text_line, match, tag)

    return new_text_line

def tag_single_match(text_line, match, tag):

    with_one_tag = insert_html('</span>', text_line, match[1])
    with_both_tags = insert_html('<span class="' + tag + '">',
        with_one_tag, match[0])

    return with_both_tags

def insert_html(insertion, string, position):
    """Insert an HTML tag into a certain position in a string."""

    return string[:position] + insertion + string[position:]

def get_matches(orig_text, compare_text, printout=False):
    """Takes two texts and returns the char ranges of matching sections.
    Uses simplified matches as described in functions below.
    Prints out the matching text if printout is True."""

    # print orig_text
    # print compare_text
    sm = difflib.SequenceMatcher(None, a=unicode(orig_text),
        b=unicode(compare_text), autojunk=False)
    output_list = simplify_match_list(sm.get_matching_blocks(), orig_text)
    # ranges = simplify_match_list(sm.get_matching_blocks(), orig_text)
    # output = [orig_text[r[0]:r[1]] for r in ranges if (r[1]-r[0] > 20)]
    total_match_length = reduce(
        (lambda x, y: x + (y[1] - y[0])), output_list, 0)

    if printout:
        # for o in output:
        #     print(o + '\n\n')
        for match_range in output_list:
            print orig_text[match_range[0]:match_range[1]] + '\n\n'

    return {
        'output_list': output_list,
        'no_match_length': (len(unicode(compare_text)) - total_match_length)
    }

def simplify_match_list(matching_blocks, source):
    """Takes a list of Match objects and simplifies it to a more consise list
    of character ranges. Includes grouping close-together sequences."""

    match_positions = get_match_positions(matching_blocks)
    simple_list = reduce(simplify_sequence, match_positions, [(0,0)])
    simple_list_stripped = [strip_junk(a, b, source) for (a, b) in simple_list]
    # if (0,0) in simple_list_stripped:
    #     simple_list_stripped.remove((0,0),)
    # for i in simple_list_stripped:
    #     if i[0] == i[1]

    # return simple_list_stripped
    return [i for i in simple_list_stripped if (i[1] - i[0] > 25)]

def simplify_sequence(x, y):
    """Groups pairs of character positions if they're close together.
    Example: [(0,25), (28,69)] -> [(0,69)]
    but [(0,25), (150,169)] -> [(0,25), (150,169)]
    Intended as a parameter for a reduce function."""

    separation_threshold = 21

    if (y[0] - x[-1][1]) <= separation_threshold:
        x[-1] = (x[-1][0], y[1])
    else:
        x.append(y)

    return x

def get_match_positions(matching_blocks):
    """Converts Match objects to their character ranges in the original text."""

    return [(i[0], i[0]+i[2]) for i in matching_blocks if (i[2] > 5)]

def strip_junk(start_pos, end_pos, source):
    """Tells how many characters to offset the beginning of a string that
    starts with junk characters that we don't want to include.
    Some of these are literal junk, while others will mess with
    Markdown formatting."""

    def expand_to_grab(list_of_snippets, char_num):
        """Will expand the selection to grab a snippet of text."""

        new_char_num = char_num
        for snippet in list_of_snippets:
            if source[new_char_num-len(snippet):new_char_num] == snippet:
                new_char_num -= len(snippet)

        return new_char_num

    text = source[start_pos:end_pos]
    # strip_length = len(text) - len(text.lstrip('.,; '))
    # print 'text'
    # print text
    stripped = re.sub(r'^ {0,8}[-.,;*#\w\d]{0,2}[-.,;*#]\d? {0,4}', '', text,
        count=1, flags=re.M)
    stripped = stripped.lstrip() # Strip any whitespace still remaining
    # print 'stripped'
    # print stripped
    # re.compile(r'\n {0,8}[-.*,;\w\d]{0,2}[-.*,;]\d? {0,4}', re.M)
    strip_length = len(text) - len(stripped)
    new_start_pos = start_pos + strip_length
    new_end_pos = end_pos
    # Don't mess up bold beginnings in Markdown:

    # print type(source)
    # print len(source)
    # print source[new_start_pos:end_pos]
    # print source[new_start_pos-1]
    # print source[new_start_pos-1].isalpha()
    while source[new_start_pos-1].isalpha():
        new_start_pos -= 1
    # while source[new_end_pos].isalpha():
    #     new_end_pos += 1
    # while source[new_start_pos-1].isalpha():
    #     if source[new_start_pos].isalpha():
    #         new_start_pos -= 1

    for snippet in ['**', '*', '<em>', '<strong>']:
        if source[new_start_pos-len(snippet):new_start_pos] == snippet:
            new_start_pos -= len(snippet)

    # if source[new_start_pos-2:new_start_pos] == '**':
    #     new_start_pos -= 2
    # if source[new_start_pos-1:new_start_pos] == '*':
    #     new_start_pos -= 1
    # if source[new_start_pos-4:new_start_pos] == '<em>':
    #     new_start_pos -= 4
    # if source[new_start_pos-8:new_start_pos] == '<strong>':
    #     new_start_pos -= 8

    for snippet in ['**', '*', '</em>', '</strong>']:
        if source[new_end_pos:new_end_pos+len(snippet)] == snippet:
            new_end_pos += len(snippet)


    # add one or two asterisks back in

    # return (start_pos + strip_length, end_pos)
    return (new_start_pos, new_end_pos)


# reduce(lambda x, y: if y[0] - x[-1][1] , seq, [(0,0)])
# reduce(simplify_sequence, seq, [(0,0)])
