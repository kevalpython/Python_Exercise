numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]
print("A. Length of the list \nB. Display first 3 numbers \nC. Display sum of odd numbers \nD. Number of duplicate numbers \nE. Display list without duplicate numbers")
print("list = ",numbers)
choice=input("enter the above options : ")
print(choice)
without_duplicate=[]
duplicate=[]
if choice == "A":
    print(len(numbers))
elif choice == "B": 
    for i in range(0,len(numbers)):
        if i <= 2:
            print(numbers[i])
elif choice == "C":
    odd_number=[]
    for i in numbers:
        if i%2!=0:
            odd_number.append(i)
    print(sum(odd_number))
elif choice == "D":
    for i in numbers:
        if i not in without_duplicate:
            without_duplicate.append(i)
        else:
            if i not in duplicate:
                duplicate.append(i)
    print(duplicate)
elif choice == "E":
    for i in numbers:
        if i not in without_duplicate:
            without_duplicate.append(i)
    print(without_duplicate)
else:
    print('"'+choice+'"'+" your enter choice is not there.")


