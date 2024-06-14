"""
Arithmetic and Geometric progression
"""

WRONG_AP = [2, 5, 8, 11, 15, 17]
WRONG_GP = [2, 4, 8, 16, 15, 64]


def arithmetic_progression(numbers):
    """
    This Function show Arithmetic progression

    number : its return the given list of numbers by user

    return : this function return the arithmetic progress of given list
    """
    common_difference = numbers[1] - numbers[0]
    for i in range(1, len(numbers) - 1):
        if numbers[i + 1] - numbers[i] != common_difference:
            wrong_index = i + 1
            break
    correct_value = numbers[i] + common_difference
    numbers[wrong_index] = correct_value
    return numbers


def geometric_progression(numbers):
    """
    This Function show Geometric progression

    number : its return the given list of numbers by user

    return : this function return the geometric progress of given list
    """
    common_ratio = numbers[1] / numbers[0]
    for i in range(1, len(numbers) - 1):
        if numbers[i + 1] / numbers[i] != common_ratio:
            wrong_index = i + 1
            break
    print(wrong_index)
    correct_value = numbers[i] * common_ratio
    numbers[wrong_index] = correct_value
    return numbers


CORRECT_AP = arithmetic_progression(WRONG_AP)
CORRECT_GP = geometric_progression(WRONG_GP)

print("Correct A.P.:", CORRECT_AP)
print("Correct G.P.:", CORRECT_GP)
