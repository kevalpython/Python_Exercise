"""
three most frequent and three least frequent names
"""

NAMES = [
    "Smith",
    "Johnson",
    "Williams",
    "Jones",
    "Brown",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
]

NAME_LENGTH = {}
for name in NAMES:
    length = len(name)
    if length in NAME_LENGTH:
        NAME_LENGTH[length].append(name)
    else:
        NAME_LENGTH[length] = [name]

SORTED_LENGTHS = sorted(NAME_LENGTH.items())
NAMES_LENGTH = []
for name in NAMES:
    NAMES_LENGTH.append(len(name))

print("Names:", NAME_LENGTH)
print("Name lengths:", NAMES_LENGTH)

print("The three most frequent name lengths are:")
for length, names_list in SORTED_LENGTHS[0:3]:
    print(f"{len(names_list)} NAMES of length {length}: {names_list}")

print("The three least frequent name lengths are:")
for length, names_list in SORTED_LENGTHS[-3:]:
    print(f"{len(names_list)} NAMES of length {length}: {names_list}")
