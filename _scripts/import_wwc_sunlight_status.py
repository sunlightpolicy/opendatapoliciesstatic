import os
import pandas
import re

# data = pandas.read_csv('../_data/city_status_data.csv')

# if its in this list, then its a WWC
# check for sunlight status



# read the data

# def 

# loop through _places

# for place in os.listdir('../_places/'):
#     if place is in data:
#         mark as WWC true
#             check for sunlight
#             if sunlight:
#                 mark policies with matching place as sunlight true
#             else:
#                 mark policies with matching place as sunlight false
#     else:
#         mark as WWC false
#         mark policies with matching place as sunlight false



def mark_matching_policies(place, boolean):

    for doc in os.listdir('../_documents/'):
        if (place + '-2') in doc:
            mark(doc, 'sunlight', boolean)

    return

def mark(filename, sunlight_or_wwc, boolean):

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

    with open(folder + filename, 'w') as my_file:
        search = re.search(r'\n' + sunlight_or_wwc + r': ', my_file)
        if search:
            print("Property '" + sunlight_or_wwc + "' found for " +
                filename + ". Value left as-is.")
        else:
            re.sub(next_text,
                '\n' + sunlight_or_wwc + ': ' + convert_bool(boolean) + '\n')

    return

def convert_bool(boolean):

    if boolean == True:
        return 'true'
    elif boolean == False:
        return 'false'
    else:
        raise Exception('Unexpected value for boolean: ' + boolean)



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
