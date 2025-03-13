# wildcard ., the symbol can take place of any other symbol
# when we want to include any random chars that may appear in out pattern

import re

string = 'acb'
pattern = r'a.b'

if re.match(pattern, string):
    print('Match found')
else:
    print('No match found')