import pandas

states = pandas.read_csv('../_data/states.csv')

for state in states.to_dict('records'):
    newfile = open('../_states/' + state['state_code'] + '.md', 'w')
    newfile.write('---' +
    	'\nstate_code: ' + state['state_code'] +
    	'\ntitle: ' + state['state_name'] +
    	'\n---\n')
    newfile.close()
