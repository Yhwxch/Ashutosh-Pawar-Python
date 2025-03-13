n = int(input('Enter numerator'))

d = int(input('Enter numerator'))

try:
    result = n/d
except ZeroDivisionError:
    print('Cannot divide a number by zero')
# the else block will only execute if the exceptions not occur 
else:
    print(result)
# the finally block will execute whichever case
finally:
    print('This code will be executed to matter what')