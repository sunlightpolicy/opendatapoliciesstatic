import os
import pandas

states = pandas.read_csv('../_data/states.csv')

# for state in states.to_dict('records'):
#     if not os.path.exists(state['state_code']):
#         os.makedirs(state['state_code'])
#     newfile = open('{0}/index.md'.format(state['state_code']), 'w')
#     newfile.write('--\nlayout: state\nstate_code: {0}\nstate_name: {1}\n--\n'
#       .format(state['state_code'], state['state_name']))


for state in states.to_dict('records'):
    newfile = open('{0}/index.md'.format(state['state_code']), 'w')
    newfile.write('--\nlayout: state\nstate_code: {0}\nstate_name: {1}\n--\n'
        .format(state['state_code'], state['state_name']))
