# A dictionary key can have sequence datatypes like list, set, tuple like below
student = {'Name': ['Lakshmi','Seetha','Rama'],
           'Age':{10,20,30},
           'email':('abc@gmail.com','xyz@gmail.com','123@gmail.com')

           }

print(type(student))
# <class 'dict'>

print(student)
# {'Name': ['Lakshmi', 'Seetha', 'Rama'], 'Age': {10, 20, 30}, 'email': ('abc@gmail.com', 'xyz@gmail.com', '123@gmail.com')}