import os
import pandas
import re


def run_through_data(data):

    for filename in os.listdir('../_places/'):
        if filename[-3:] == '.md':  # if it's really one of the place files
            with open('../_places/' + filename, 'r') as my_file:
                contents = my_file.read()
                place_pretty, place_id = get_place_names(contents)
            if place_pretty in data['CityAndState'].values:
                mark(filename, 'wwc', 'true')
                place_info = data[data['CityAndState'] == place_pretty]
                if len(place_info) != 1:
                    raise Exception('Found ' + sun + ' matches for ' +
                        place_pretty)
                sunlight = place_info['Sunlight'].item()
                if sunlight:
                    mark_matching_policies(place_id, 'true')
                else:
                    mark_matching_policies(place_id, 'false')
            else:
                mark(filename, 'wwc', 'false')
                mark_matching_policies(place_id, 'false')

    return

def get_place_names(file_contents):

    place_title = re.search(r'(?<=title: ).+(?=\n)', file_contents).group()
    place_state = re.search(r'(?<=states:\n  - )\w{2}', file_contents).group()
    place_pretty = place_title + ', ' + place_state

    place_id = re.search(r'(?<=place: ).+(?=\n)', file_contents).group()

    return (place_pretty, place_id)

def mark_matching_policies(place, boolean_string):

    for doc_name in os.listdir('../_documents/'):
        if (place + '-2') in doc_name:
            mark(doc_name, 'sunlight', boolean_string)

    return

def mark(filename, sunlight_or_wwc, boolean_string):

    if sunlight_or_wwc == 'sunlight':
        folder = '../_documents/'
        next_text = r'\n(?=portal_url)'
    elif sunlight_or_wwc == 'wwc':
        folder = '../_places/'
        next_text = r'\n(?=---)'
    else:
        raise Exception(sunlight_or_wwc +
            ' is not a valid value for sunlight_or_wwc\n(Error found for ' +
            filename + ')')

    with open(folder + filename, 'r') as old_file:
        contents = old_file.read()
        search = re.search(r'\n' + sunlight_or_wwc + r': ', contents)
        if search:
            print("Property '" + sunlight_or_wwc + "' found for " +
                filename + ". Value left as-is.")
            new_contents = contents
        else:
            new_contents = re.sub(next_text,
                '\n' + sunlight_or_wwc + ': ' + boolean_string + '\n',
                contents)

    with open(folder + filename, 'w') as new_file:
        new_file.write(new_contents)

    return


if __name__ == '__main__':
    run_through_data(pandas.read_csv('../_data/city_status_data.csv'))


# def convert_bool(boolean):

#     if boolean == True:
#         return 'true'
#     elif boolean == False:
#         return 'false'
#     else:
#         raise Exception('Unexpected value for boolean: ' + boolean)



# # for state in states.to_dict('records'):
# #     newfile = open('../_states/' + state['state_code'] + '.md', 'w')
# #     newfile.write('---' +
# #         '\nstate_code: ' + state['state_code'] +
# #         '\ntitle: ' + state['state_name'] +
# #         '\n---\n')
# #     newfile.close()


# for doc in os.listdir('../_documents/'):
#     with open('../_documents/' + doc, 'r') as infile:
#         text = infile.read()
#         get = make_get_function(doc, text)
#         loc = get(r'(?<=title: ).+?(?=\()')
#         try:
#             city, state = [i.strip() for i in loc.split(',')]
#         except ValueError:
#             print 'Error when grabbing city, state from ' + doc
#         else:
#             place = city.lower().replace(' ', '-') + '-' + state.lower()
#             year = get(r'\d{4}(?=.+?Link)')
#             legal_custom = get(r'(?<=Means:( |\n)).+?(?=\',)')
#             policy_url = get(r'(?<=Link: ).+?(?=;.+?Means:)')
#             validate_url(policy_url)
#             content = re.search(r'(?<=\n---\n).+', text, re.DOTALL).group()
#             with open('../_documents/' + place + '-' + year + '.md',
#                 'w') as outfile:
#                 outfile.write('---' +
#                     '\nplace: ' + place +
#                     '\nyear: ' + year +
#                     '\nlegal_custom: ' + legal_custom +
#                     '\npolicy_url: ' + policy_url +
#                     '\n---\n' + content + '\n')
