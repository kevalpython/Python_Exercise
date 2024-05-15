numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n = 12
res = []
for i in range(len(numbers)):
    index=i
    for j in range(i+1,len(numbers)):
        total=numbers[index] + numbers[j]
        if total==n:
            if (numbers[index],numbers[j]) not in res and (numbers[j],numbers[index]) not in res:
                res.append((numbers[index],numbers[j]))
print(res)