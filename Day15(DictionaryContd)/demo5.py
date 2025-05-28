# Nested dictionary

# syntax:
# dict1 = {
#         key:{key:value,key:value},
#         key:{key:value,key:value},
#         key:{key:value,key:value}
#         }

nd = {
        1:{2:'red',3:'blue'},
        4:{5:'pink',6:'orange'},
        7:{8:'white',9:'black'}
    }

print(nd)
# {1: {2: 'red', 3: 'blue'}, 4: {5: 'pink', 6: 'orange'}, 7: {8: 'white', 9: 'black'}}

print(nd[1])
# {2: 'red', 3: 'blue'}

print(nd[1][3])
# blue

print(nd[7][8])
# white

print(nd[4].keys())
# dict_keys([5, 6])

print(nd[4].values())
# dict_values(['pink', 'orange'])

print(nd[4].items())
# dict_items([(5, 'pink'), (6, 'orange')])