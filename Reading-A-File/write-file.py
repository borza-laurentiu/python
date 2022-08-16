employee_file = open("employees.txt", "w")  #overwrites the file

new_entry = input("Enter a new entry: ")
employee_file.write("\n" + new_entry)
employee_file.close()