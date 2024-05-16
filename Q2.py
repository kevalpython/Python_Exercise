names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson',
         'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

name_lengths = {}
for name in names:
    length = len(name)
    if length in name_lengths:
        name_lengths[length].append(name)
    else:
        name_lengths[length] = [name]

sorted_lengths = sorted(name_lengths.items())
names_length=[]
for name in names:
    names_length.append(len(name))
    
print("Names:", name_lengths)
print("Name lengths:", names_length)

print("The three most frequent name lengths are:")
for length, names_list in sorted_lengths[0:3]:
    print(f"{len(names_list)} names of length {length}: {names_list}")
    
print("The three least frequent name lengths are:")
for length, names_list in sorted_lengths[-3:]:
    print(f"{len(names_list)} names of length {length}: {names_list}")