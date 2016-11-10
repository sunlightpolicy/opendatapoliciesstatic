import os
import pandas

states = pandas.read_csv('../_data/states.csv')

for state in states['state_code']:
    if not os.path.exists(state):
        os.makedirs(state)
    newfile = open('{0}/index.md'.format(state), 'w')
    newfile.write('--\nstate_code: {0}\n--\n'.format(state))
