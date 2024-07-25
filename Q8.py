"""
Sorting List
"""


def sorting(array, size):
    """
    this function sort the given array 
    
    args : arrays = give the list of number which we have to sort 
           size = give the array length
    
    this function return the sorted array of given array
    """
    for i in range(size):
        index = i
        for j in range(i + 1, size):
            if array[j] < array[index]:
                index = j
            (array[i], array[index]) = (array[index], array[i])
    print(array)


DATA = [1, 4, 2, 7, 8, 6, 3]
SIZE = len(DATA)
print(DATA)
print("With selection sort.")
sorting(DATA, SIZE)
