# Another example

class Car:
    car_Name = 'BMW'
    car_color = 'White'
    car_price = 500000
    car_type = 'petrol'


car_obj = Car()
print(car_obj.car_Name)
print(car_obj.car_color)
print(car_obj.car_price)
print(car_obj.car_type)

print()
# to update values
car_obj.car_Name = 'AUDI'
car_obj.car_color = 'Black'
car_obj.car_price = 1000000

print(car_obj.car_Name)
print(car_obj.car_color)
print(car_obj.car_price)
print(car_obj.car_type)

print('Delete a value')
# To delete a variable/value
del car_obj.car_type

print(car_obj.car_Name)
print(car_obj.car_color)
print(car_obj.car_price)
print(car_obj.car_type)
# BMW
# White
# 500000
# petrol
#
# AUDI
# Black
# 1000000
# petrol

# Delete a value
# AttributeError: 'Car' object has no attribute 'car_type'

# One more instance:
car_obj1 = Car()
car_obj1.car_Name = 'HONDA'