import pandas

states = pandas.read_csv('../_data/states.csv')

for i in states['state_code']:
    newfile = open('{0}.md'.format(i), 'w')
    newfile.write('--\nstate_code: {0}\n--\n'.format(i))
