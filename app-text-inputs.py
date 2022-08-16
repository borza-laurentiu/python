from datetime import datetime

# print('Enter your First Name:')
# first_name = input()
first_name = input('Enter your First Name:')
last_name = input('Enter your Last Name:')
YOB = input('Enter your Year Of Birth:')
print('Hello, ' + first_name + ' ' + last_name)

name = first_name + ' ' + last_name
print(f'{name} was born in 1981')


now = datetime.utcnow().year
age = now - int(YOB)
ageInMonths = age*12
print(f'Hello {name}, you are {ageInMonths} months old')

