"""
Find pairs in list whose sum equal to given number
"""

NUMBERS = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
NUM = 12
RESULT = []
for i in range(len(NUMBERS)):
    index = i
    for j in range(i + 1, len(NUMBERS)):
        total = NUMBERS[index] + NUMBERS[j]
        if total == NUM:
            if (NUMBERS[index], NUMBERS[j]) not in RESULT and (
                NUMBERS[j],
                NUMBERS[index],
            ) not in RESULT:
                RESULT.append((NUMBERS[index], NUMBERS[j]))
print(RESULT)
