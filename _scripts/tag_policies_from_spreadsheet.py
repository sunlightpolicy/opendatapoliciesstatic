import difflib
import gfm
import pandas as pd
import re
import regex
import us

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


def convert_name(name):

    if ',' in name:
        parts = re.search(
            r'(.+?)((( and )|-|/)\w+ County)?, ([A-Z])\.?([A-Z])\.?', name)
        return (parts.group(1).lower().replace(' ', '-') + '-' +
            parts.group(5).lower() + parts.group(6).lower())
    else:
        return us.states.lookup(unicode(name)).abbr.lower()


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

def tag_items(orig_text_list, compare_text, tag):
    """Go through a doc looking for matches for a single definition."""

    new_text_list = orig_text_list[:]
    for x in range(len(new_text_list)):
        line_matches = get_matches(new_text_list[x], compare_text)
        new_text_list[x] = tag_all_matches(new_text_list[x], line_matches, tag)
        # for match in line_matches:
        #     line_w_end_tag = insert_html(</, line, match[1])
        #     line_w_both_tags = insert_html(, match[0])
        # line = line_w_both_tags

    return new_text_list

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

    return string[:position] + insertion + string[position:]

def get_matches(orig_text, compare_text, printout=False):
    """Takes two texts and returns the char ranges of matching sections.
    Uses simplified matches as described in functions below.
    Prints out the matching text if printout is True."""

    sm = difflib.SequenceMatcher(None, a=orig_text,
        b=compare_text, autojunk=False)
    output = simplify_match_list(sm.get_matching_blocks(), orig_text)
    # ranges = simplify_match_list(sm.get_matching_blocks(), orig_text)
    # output = [orig_text[r[0]:r[1]] for r in ranges if (r[1]-r[0] > 20)]

    if printout:
        # for o in output:
        #     print(o + '\n\n')
        for match_range in output:
            print orig_text[match_range[0]:match_range[1]] + '\n\n'

    return output

def simplify_match_list(matching_blocks, source):
    """Takes a list of Match objects and simplifies it to a more consise list
    of character ranges. Includes grouping close-together sequences."""

    match_positions = get_match_positions(matching_blocks)
    simple_list = reduce(simplify_sequence, match_positions, [(0,0)])
    simple_list_stripped = [strip_left_junk(a, b, source) for (a, b) in simple_list]
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

    separation_threshold = 7

    if (y[0] - x[-1][1]) <= separation_threshold:
        x[-1] = (x[-1][0], y[1])
    else:
        x.append(y)

    return x

def get_match_positions(matching_blocks):
    """Converts Match objects to their character ranges in the original text."""

    return [(i[0], i[0]+i[2]) for i in matching_blocks if (i[2] > 5)]

def strip_left_junk(start_pos, end_pos, source):
    """Tells how many characters to offset the beginning of a string that
    starts with junk characters that we don't want to include.
    Some of these are literal junk, while others will mess with
    Markdown formatting."""

    text = source[start_pos:end_pos]
    # strip_length = len(text) - len(text.lstrip('.,; '))
    # print 'text'
    # print text
    stripped = re.sub(r'^ {0,8}[-.,;*\w\d]{0,2}[-.,;*]\d? {0,4}', '', text,
        count=1, flags=re.M)
    # print 'stripped'
    # print stripped
    # re.compile(r'\n {0,8}[-.*,;\w\d]{0,2}[-.*,;]\d? {0,4}', re.M)
    strip_length = len(text) - len(stripped)
    new_start_pos = start_pos + strip_length
    # Don't mess up bold beginnings in Markdown:
    if source[new_start_pos-2:new_start_pos] == '**':
        new_start_pos -= 2
    elif source[new_start_pos-1:new_start_pos] == '*':
        new_start_pos -= 1

    # add one or two asterisks back in

    # return (start_pos + strip_length, end_pos)
    return (new_start_pos, end_pos)


# reduce(lambda x, y: if y[0] - x[-1][1] , seq, [(0,0)])
# reduce(simplify_sequence, seq, [(0,0)])
