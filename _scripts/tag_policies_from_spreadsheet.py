import pandas as pd
import re
import regex
import us

# pd.read_csv
# actually read excel

def try_to_match(input_str, reference_str):
    """Will test an exact match, then an exact match with quotation marks
    removed, then a close match (no more than 4 characters off), then
    a match within quotation marks (like if there's explanatory text)."""

    if input_str in reference_str:
        return true
    elif input_str.strip('"') in reference_str:
        return true
    elif regex.search(r'(?:' + regex.escape(input_str) + r'){e<=4}', reference_str):
        return true
# add something where you try stripping out HTML?



Notes:

Need to convert 'n/a' to no
Convert blank to unknown... or no?
Use Joyce/Wenjia notes to compare

Do something special if contains 'close fit'

Need to figure out how to deal with HTML
Multiparagraph? Maybe have a tiered system:
    Convert to HTML (if Markdown)
    If quote in text, then tag it
    If quote not in text, then go paragraph by paragraph, and check for overlap against the quote

Need a special tag for opposite/negative answers

Someday need a function to check which guidelines a policy meets



for block in text:
    convert to plain text?
    check for a common substring with spreadsheet cell
    if common substring:
        tag the whole block
        # handle complicated situations


def find_place(converted_name):



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


need definitions for Data, Public Data/Information, Open Data

