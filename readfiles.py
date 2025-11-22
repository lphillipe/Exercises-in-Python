

employees_file = open("employees.txt", "r")
for line in employees_file.readlines():
    print(line)



employees_file.close()