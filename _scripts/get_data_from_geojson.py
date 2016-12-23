import frontmatter
import json
import os


# Primary functions

def main():

    return

def 


with open('../_old/USlocalpolicylocations.geojson') as read_file:
    places = [i['properties'] for i in json.loads(read_file)['features']]

def process_doc():

    If placename in doc title
        # Date stuff
        If date field already exists
            See if it matches info from geojson; if not, print a warning message
        Elif date field exists in geojson data
            Make that the date for the policy
        Else 
            Use policy year for the date
            Print a warning message
        Delete year
        # Other stuff
        for v in ['policy_url', 'legal_custom']:
            check_var(placename, v, doc_dict, ref_dict)

    return

def check_var(placename, var_name, doc_dict, ref_dict):

    if var_name in ref_dict:
        if ref_dict[var_name] != doc_dict[var_name]:
            print('For ' + placename + ', ' + var_name + ' did not match.' +
                '\nDoc metadata value: ' + doc_dict[var_name] +
                '\nGeoJSON value: ' + ref_dict[var_name] + '\n')
    else:
        print('For ' + placename + ', ' + var_name + ' not found in GeoJSON.')

    return

# Secondary functions

def make_placename(city_or_county, state_code):

    return city_or_county.lower().replace(' ', '-') + '-' + state_code.lower()

def convert_date(mmddyyyy):

    split_date = mmddyyyy.split('/')
    yyyymmdd = split_date[2] + '-' + split_date[0] + '-' + split_date[1]

    return yyyymmdd

def make_vars(place):

    if 'City' in place:
        place['placename'] = make_placename(place['City'], place['State'])
    elif 'County' in place:
        place['placename'] = make_placename(place['County'], place['State'])
    else:
        place['placename'] = place['State'].lower()
    place['date'] = convert_date(place['Date'])
    place['legal_custom'] = place['Legal Means']
    place['states'] = [place['State']]
    place['policy_url'] = place['Policy URL']
    place['wwc'] = place['WWC'].lower()  # Will convert to boolean in YAML

    return place



# NOTE: place all docs in a new folder

Loop through places
    For doc in docs

    For _places[place]:
        check_var(place, 'wwc', _places[place], geo[place])

Compile list of docs and places that were checked so we can see if they all were

# Run

if __name__ == '__main__':
    main()
