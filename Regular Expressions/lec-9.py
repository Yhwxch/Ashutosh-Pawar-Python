# [] takes a range of chars that are acceptable in the pattern [a-zA-z], [0-9], [aACrf]....

import re

string = 'python'
pattern = r'[A-za-z]'

if re.match(pattern, string):
    print('Match found')
else:
    print('No match found')