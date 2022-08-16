myList = [1,2,3,4,5,6, 4, 20, 25, 6]

myList.insert(2, 3.5)
myList.append(6.5)

print(myList)

emptyList = []

listLower = []
listHigher = []

for i in myList:
    if i % 2 == 0:
        emptyList.append(i)

print(emptyList)

def sort(list): 
    #set the length as a variable
    l = len(list)
    if l <= 1 : 
        return list #if 1 or fewer numbers, return the number
    else:
        p = list.pop() #take each number from given input
    for i in list: #loop through given list  sort(list)
        if l > p:
            listHigher.append(i)
        else:
            listLower.append(i)
    return sort(listLower) + [p] + sort(listHigher)
