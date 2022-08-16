inputList = [1,2,3,4,5]
print(str(inputList))
newList = []
print(str(newList))

for number in inputList:
    if number % 2 == 0: 
        newList.insert(1,number)

print(str(newList))


#create an array/list with at least 5 numbers. Write a function that checks 
#for even numbers and populates them into a new list (hint: you will need to create an empty array/list also)