# Print only dose food from the below list
food = ['Masala dose','Pongal','Rava dose','upma','Khali dose','idly','Open Dose','Plain dose']

dose_list = []

for i in food:
    if 'dose' in i.lower():
        dose_list.append(i)


print(dose_list)
# ['Masala dose', 'Rava dose', 'Khali dose', 'Open Dose', 'Plain dose']