import datetime

t_date = datetime.datetime.now()
print(type(t_date))
# <class 'datetime.datetime'>
print(t_date)
# 2025-05-26 14:37:58.686057

print(datetime.datetime.today())
# 2025-05-26 14:38:25.262746

print(t_date.day)
print(t_date.hour)
print(t_date.minute)
print(t_date.second)

# 26
# 14
# 40
# 2

