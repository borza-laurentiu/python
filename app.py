from datetime import datetime

my_list = [8, 1, 3, 6, 88, 4]
print(my_list[1])
my_list.sort()
print(my_list)
print(my_list[1])
my_list[2] = 32
print(my_list)
print('Hello' + str(my_list) + 'goodbye')

a = 5
b = 10
prod = a * b
print(2*prod)

date = 1992
date = str(date)       #casting
name = 'John'
now = datetime.utcnow().year
myDOB = 1986
age = now - myDOB

print(name,'was born in', date)   #concatenation
print(name + ' was born in ' + date)   #concatenation

date = 1992
print(f'{name} was born in {date}')   #concatenation  #f=format (it formats the date too, no need for str)

print(age)

myNewList = [1,2,3,4,5,6,7,8,9,10]

#set counter to 0
count = 0

#iterate or loop over the entire myNewList
for myItem in myNewList:
    #check for remainder to detect even numbers 
    if myItem % 2 == 0: 
        #for every even number, increment counter
        count +=1

print(count)

IdRequired = 'ID Required'
NoIdRequired = 'No ID Required'

age = int(input("Please enter your age: "))

appearance = int(input("Please enter how old you look: "))

if (age >= 18 and age <= 25) and (appearance >=25):
    print(NoIdRequired)
elif (age >= 18 and age <=25) and (appearance < 25):
    print(IdRequired)
# else:

a = int(input("enter: "))
res = f'The  product of {a} is {a*100}'
print(res)

def hello():
    return "Hello"

print(hello())



