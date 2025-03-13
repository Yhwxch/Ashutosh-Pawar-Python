import re

string = 'abc'
pattern = 'a'
# works like startswith
print(re.match(pattern, string))

if re.match(pattern, string):
    print('Match found')
else:
    print('No match found')