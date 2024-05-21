# 1
n = 3

for i in range(1, n + 1):
    print("*" * (n - i), end="")
    for k in range(1, i * 2):
        print(" ", end="")
    print("*" * (n - i), end="")
    print()

for i in range(n - 1, 0, -1):
    print("*" * (n - i), end="")
    for k in range(1, i * 2):
        print(" ", end="")
    print("*" * (n - i), end="")
    print()

# 2
n = 3

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for k in range(1, i * 2):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for k in range(1, i * 2):
        print("*", end="")
    print()

# 3
n = 5

for i in range(1, n+1):
    counter = 0
    for j in range(i):
        if j == 0 or j == i-1:
            print("*", end='')
            counter += 1
        else:
            if i != n:
                print(' ', end='')
            else:
                print("*", end='')
                counter += 1
    print()
 
# 4
n = 5 

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 5
n = 5
num = 1
for i in range(0, n):
    for j in range(0, i+1):
        print(num, end=" ")
        num += 1
    print()