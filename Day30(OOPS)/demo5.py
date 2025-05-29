# Instance methods
# Calling Instance Variables by using Instance methods
# Instance method: Used to access or modify the object state. If we use instance variables inside a method,
# such methods are called instance methods. It must have a self parameter to refer to the current object.

# self: The first argument self refers to the current object.
# It binds the instance to the __init__() method.
# It’s usually named self to follow the naming convention.

class Mobile:

    # Constructor
    def __init__(self,m_name, m_RAM, m_color, m_price, m_Mfg):
        self.name = m_name
        self.RAM = m_RAM
        self.color = m_color
        self.price = m_price
        self.Mfg = m_Mfg


    # Instance method: Has instance variables
    def display(self):
        print(f'Name:{self.name}')
        print(f'RAM:{self.RAM}')
        print(f'Color:{self.color}')
        print(f'Manufacturing:{self.Mfg}')


obj_IPhone = Mobile('IPhone',8,'white',100000,2025)
obj_IPhone.display()

# Name:IPhone
# RAM:8
# Color:white
# Manufacturing:2025
print()
obj_Samsung = Mobile('Samsung',16,'pink',40000,2025)
obj_Samsung.display()

# Name:Samsung
# RAM:16
# Color:pink
# Manufacturing:2025

