# any code that could cause an error it should be put inside try/except block

n = int(input('Enter numerator'))

d = int(input('Enter numerator'))

result = 0

try:
    result = n/d
except ZeroDivisionError:
    print('Cannot divide a number by zero')

print(result)