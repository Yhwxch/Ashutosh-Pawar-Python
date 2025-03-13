# ^ the patter should start  with the chars preceding it

import re

string = '9123839282'
pattern = r'^91'

if re.match(pattern, string):
    print('Match found')
else:
    print('No match found')