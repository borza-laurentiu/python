# employee_file = open("employees.txt", "r")   #r stands for read-only, r+ stands for read and write
# print(employee_file.readable())  #checks if it can read the file and returns TRUE

# employee_file = open("employees.txt", "w")
# print(employee_file.readable())   #checks if it can read the file and returns FALSE because of the "w" = write parameter

#the above commands also seem to delete the content of the txt file

employee_file = open("employees.txt", "r") 
# print(employee_file.read())       #reads the entire file and displays it
# print(employee_file.readline())   #reads the 1st line
# print(employee_file.readline())   #reads the 2nd line
print(employee_file.readlines()[1])   #this one doesnt work if there is a read command called before
employee_file.close()  #close the file