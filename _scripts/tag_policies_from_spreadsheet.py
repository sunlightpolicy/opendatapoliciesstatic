import difflib
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




# MD -> HTML
# Go from beginning to end, stripping out HTML, and adding those tags to a dict that knows the beginning character position
# Compare strings and get matches

# deal with 'Does the opposite' and 'close fit'

def get_matches(original_text, compare_text, printout=False):
    """Takes two texts and returns the char ranges of matching sections.
    Uses simplified matches as described in functions below.
    Prints out the matching text if printout is True."""

    sm = difflib.SequenceMatcher(None, a=original_text,
        b=compare_text, autojunk=False)
    output = simplify_match_list(sm.get_matching_blocks(), original_text)

    if printout:
        for match_range in output:
            print original_text[match_range[0]:match_range[1]] + '\n\n'

    return

def simplify_match_list(matching_blocks, source):
    """Takes a list of Match objects and simplifies it to a more consise list
    of character ranges. Includes grouping close-together sequences."""

    match_positions = get_match_positions(matching_blocks)
    simple_list = reduce(simplify_sequence, match_positions, [(0,0)])
    simple_list_stripped = [strip_left_junk(a, b, source) for (a, b) in simple_list]
    if (0,0) in simple_list_stripped:
        simple_list_stripped.remove((0,0),)

    return simple_list_stripped

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

    return [(i[0], i[0]+i[2]) for i in matching_blocks]

def strip_left_junk(start_pos, end_pos, source):
    """Tells how many characters to offset the beginning of a string that
    starts with junk characters that we don't want to include."""

    text = source[start_pos:end_pos]
    strip_length = len(text) - len(text.lstrip('.,; '))

    return (start_pos + strip_length, end_pos)


# reduce(lambda x, y: if y[0] - x[-1][1] , seq, [(0,0)])
# reduce(simplify_sequence, seq, [(0,0)])
