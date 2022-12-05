import pandas 
import numpy
import re
import os 
fo = open('paper.md', 'w')

for home, dirs, files in os.walk('.'):
    for file in files:
        file_name = file.split('.')[0]
        file_type = file.split('.')[1]

        if file_type != 'xlsx':
            continue

        data = pandas.read_excel(file_name + '.xlsx', index_col=None, header=None)

        fo.write('\n# ' + file_name.replace('_', ' ') + '\n')

        fo.write('|| Paper Title | Note | Date |\n')
        fo.write('| --- | --- | --- | --- |\n')
        print(data)

        for i in range(len(data)):
            fo.write(' | ' + str(i + 1))

            paper_name = data.iloc[i][0]
            paper_src = 'paper/' + paper_name.replace(' ', '_') + '.pdf'
            fo.write(' | '  + '[' + paper_name + ']' + '(' + paper_src + ')')
            fo.write(' | ' + data.iloc[i][2])
            fo.write(' | ' + str(data.iloc[i][1]))
            fo.write(' |\n')

        
    break
fo.close()