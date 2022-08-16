employee_file = open("employees.txt", "a")  #appends a file by adding a new line
employee_file.write("\nToby - Executive")
new_entry = input("Enter a new entry: ")
employee_file.write("\n" + new_entry)
employee_file.close()