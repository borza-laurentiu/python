# write a function that checks if a number is prime or not
# it must check all cases, to see if the number is 0, 1, 2 or negative

number = int(input('Enter a number: '))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print (f'{number} is not a prime number') 
        else:
            print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')