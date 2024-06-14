"""
Pattern Programming
"""

# 1
NUMBER = 3

for i in range(1, NUMBER + 1):
    print("*" * (NUMBER - i), end="")
    for k in range(1, i * 2):
        print(" ", end="")
    print("*" * (NUMBER - i), end="")
    print()

for i in range(NUMBER - 1, 0, -1):
    print("*" * (NUMBER - i), end="")
    for k in range(1, i * 2):
        print(" ", end="")
    print("*" * (NUMBER - i), end="")
    print()

# 2
NUMBER2 = 3

for i in range(1, NUMBER2 + 1):
    print(" " * (NUMBER2 - i), end="")
    for k in range(1, i * 2):
        print("*", end="")
    print()

for i in range(NUMBER2 - 1, 0, -1):
    print(" " * (NUMBER2 - i), end="")
    for k in range(1, i * 2):
        print("*", end="")
    print()

# 3
NUMBER3 = 5

for i in range(1, NUMBER3 + 1):
    COUNTER = 0
    for j in range(i):
        if j in (0, i - 1):
            print("*", end="")
            COUNTER += 1
        elif i == NUMBER3:
            print("*", end="")
            COUNTER += 1
        else:
            print(" ", end="")
    print()

# 4
NUMBER4 = 5

for i in range(1, NUMBER4 + 1):
    for j in range(1, NUMBER4 + 1):
        if i == 1 or i == NUMBER4 or j == 1 or j == NUMBER4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 5
NUMBER5 = 5
NUM = 1
for i in range(0, NUMBER5):
    for j in range(0, i + 1):
        print(NUM, end=" ")
        NUM += 1
    print()
