# **kwargs → Variable-length keyword arguments (Dictionary)
# Using **kwargs (Multiple Keyword Arguments)
# ✅ Allows a function to accept any number of keyword arguments.
# ✅ Collects them into a dictionary.

def info(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')


info(name='Lakshmi',age=20,salary=70000,company='Microsoft')

# name:Lakshmi
# age:20
# salary:70000
# company:Microsoft

print()
info(id=1234,branch='CS',lcoation='AP')
# id:1234
# branch:CS
# lcoation:AP


print()
# Using *args and **kwargs
def display_info(title,*args,**kwargs):
    print(f'Title:{title}')
    print('Args',args)
    print('Kwargs',kwargs)


display_info('StudentInfo','Test',25,40000,'TCS', name='Rama',id=2345,branch='EC',location='Kar')

# Title:StudentInfo
# Args ('Test', 25, 40000, 'TCS')
# Kwargs {'name': 'Rama', 'id': 2345, 'branch': 'EC', 'location': 'Kar'}




