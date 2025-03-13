# {} tells the computer to repeat the preceding character, as many number of times as the value inside the brackets

# we can also provide a minimum value for repeating

import re

string = 'abbbbbbbc'
pattern = r'ab{2,}c'

if re.match(pattern, string):
    print('Match found')
else:
    print('No match found')