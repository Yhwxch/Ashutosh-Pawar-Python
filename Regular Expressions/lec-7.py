# ? optional, it may or may not be present 

import re

string = 'python  file'
pattern = r'python.*?file'

if re.match(pattern, string):
    print('Match found')
else:
    print('No match found')