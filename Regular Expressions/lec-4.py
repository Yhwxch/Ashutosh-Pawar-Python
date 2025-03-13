# metacharacters allow us to create complex  patterns which can be match, instead of simply matching simple strings

# metacharacters: * + {...} . ? ^

# + has to be present at least once

# * ensures a particular character preceding it present 0 or more times

# in order to get successful match in the below example it has to be:
# a(any occurrence of b)c



import re

string = 'abbbbbc'
pattern = r'ab*c'

if re.match(pattern, string):
    print('Match found')
else:
    print('No match found')
