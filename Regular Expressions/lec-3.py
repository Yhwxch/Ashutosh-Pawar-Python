import re

string = 'bca'
pattern = 'a'
# scan the entire string and try look for the pattern regardless of it's position
print(re.search(pattern, string))

if re.search(pattern, string):
    print('Match found')
else:
    print('No match found')