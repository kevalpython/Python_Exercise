wrong_AP = [2, 5, 8, 11, 15, 17]
wrong_GP = [2, 4, 8, 16, 15, 64 ]

def arithmetic_progression(numbers):
    common_difference = numbers[1] - numbers[0]
    for i in range(1, len(numbers) - 1):
        if numbers[i + 1] - numbers[i] != common_difference:
            wrong_index = i+1
            break
    correct_value = numbers[i] + common_difference
    numbers[wrong_index] = correct_value
    return numbers

def geometric_progression(numbers):
    common_ratio = numbers[1] / numbers[0]
    for i in range(1, len(numbers) - 1):
        if numbers[i + 1] / numbers[i] != common_ratio:
            wrong_index = i+1
            break
    print(wrong_index)
    correct_value = numbers[i] * common_ratio
    numbers[wrong_index] = correct_value
    return numbers

correct_AP = arithmetic_progression(wrong_AP)
correct_GP = geometric_progression(wrong_GP)

print("Correct A.P.:", correct_AP)
print("Correct G.P.:", correct_GP)