import re
import os

folder = os.path.join('..', '_documents')
for doc in os.listdir(folder):
    if doc[-3:] == '.md':
        with open(os.path.join(folder, doc), 'r') as infile:
            # contents_0 = infile.read().decode('utf-8')
            # contents_1 = re.sub(r'(?<=\nsunlight: )true(?=.+\n---\n)',
            #     'wwc', contents_0, re.DOTALL)
            # contents_2 = re.sub(r'(?<=\nsunlight: )false(?=.+\n---\n)',
            #     'no', contents_1, re.DOTALL)
            # print(len(contents_0) - len(contents_2))
                        # contents_0 = infile.read().decode('utf-8')
            contents_0 = infile.read().decode('utf-8')
            contents_1 = contents_0.replace('\nsunlight: false\n', '\nsunlight: didnt\n')
            contents_2 = contents_1.replace('\nsunlight: true\n', '\nsunlight: wwc\n')
        with open(os.path.join(folder, doc), 'w') as outfile:
            outfile.write(contents_2.encode('utf-8'))
