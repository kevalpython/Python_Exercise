"""
Occurance of substring in the given string.
"""

STRING = "PQRQRQRQ"
SUBSTRING = "PQR"
STRING_LEN = len(STRING)
SUBSTRING_LEN = len(SUBSTRING)
j = 0
COUNT = 0
while j < STRING_LEN:
    if STRING[j] == SUBSTRING[0]:
        if STRING[j : j + SUBSTRING_LEN] == SUBSTRING:
            COUNT += 1
    j += 1
print(COUNT)
