numbers = [42,35,7,91,13,16]
friends = ["gigi", "jim", "oscar", "george"]
print (len(numbers))   #prints the length
print(numbers)
friends.extend(numbers)
print(friends)
friends.append("apollo")  #adds at the end
print(friends)
friends.insert(1, "Kelly")  #adds kelly on position 1
print(friends)
friends.remove("Kelly")
print(friends)
friends.pop()  #removes the last element of the list
print (friends.index("oscar"))
friends.insert(4, "oscar")
print (friends.count("oscar"))  #counts how many oscars are in the list
friends.clear()   #clears the list
print (numbers.sort())
