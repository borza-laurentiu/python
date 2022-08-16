varA = 'hello'
varA = list(varA)

count = 0
for letter in varA:
    if letter == 'l':
        count += 1

print(count)

def mult(a,b):
    return a * b

a = 1
b = 4

print(mult(a,b))

while True: 
    def fizzBuzz(number):
        fizzBuzz = ''
        if number % 5 == 0 and number % 3 == 0:
            fizzBuzz = 'fizzBuzz'
        elif number == 5 or number % 5 == 0:
            fizzBuzz = 'buzz'
        elif number == 3 or number % 3 == 0:
            fizzBuzz = 'fizz'
        else:
            fizzBuzz = 'none'
        return fizzBuzz 

    number = int(input('Enter a number: '))
    print (fizzBuzz(number))

    cont = input("Do you want to continue? y for yes only ")
    if cont != 'y':
        break
    else:   
        pass 
