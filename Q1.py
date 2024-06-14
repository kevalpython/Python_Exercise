"""
List of 10 numbers and show the 5 different operations options 
"""

NUMBERS = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]
print(
    "A. Length of the list\nB. Display first 3 numbers\nC. Display sum of odd numbers\nD. Number of duplicate numbers\nE. Display list without duplicate numbers"
)
print("list =", NUMBERS)
CHOICE = input("Enter the above options: ").upper()
print(CHOICE)
WITHOUT_DUPLICATE = []
DUPLICATE = []
if CHOICE == "A":
    print(len(NUMBERS))
elif CHOICE == "B":
    for index, number in enumerate(NUMBERS):
        if index < 3:
            print(number)
elif CHOICE == "C":
    odd_sum = sum(number for number in NUMBERS if number % 2 != 0)
    print(odd_sum)
elif CHOICE == "D":
    for number in NUMBERS:
        if NUMBERS.count(number) > 1 and number not in DUPLICATE:
            DUPLICATE.append(number)
    print(DUPLICATE)
elif CHOICE == "E":
    for number in NUMBERS:
        if number not in WITHOUT_DUPLICATE:
            WITHOUT_DUPLICATE.append(number)
    print(WITHOUT_DUPLICATE)
else:
    print(f'"{CHOICE}" your entered choice is not there.')
