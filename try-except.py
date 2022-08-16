try:
    x = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:   #catch the error and filtering it out, checking if its a zero division error
    print(err)
except ValueError:
    print("invalid Input")