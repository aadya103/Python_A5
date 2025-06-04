st_dict = {"Alice" : 85,
           "Grace" : 77,
           "Delilah" : 92
           }
name = input("Enter the student's name: ")
print(st_dict.get(name, "Student not found."))