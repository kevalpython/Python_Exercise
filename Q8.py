def sorting(array,size):
    for i in range(size):
        index=i
        for j in range(i+1,size):
            if array[j] < array[index]:
                index=j
            (array[i],array[index])=(array[index],array[i])
    print(array)
data=[1,4,2,7,8,6,3]
size=len(data)
print(data)
print("With selection sort.")
sorting(data,size)