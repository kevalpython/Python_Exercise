"""
Method and lambda operatons on Numbers
"""

from functools import reduce


class Number:
    """
    this class do some opertion on given numbers of list
    """

    def __init__(self, numbers):
        """
        this method is constructor

        numbers = given number of list which is provided by the user
        """
        self.numbers = numbers

    def get(self):
        """
        this method take the list of number

        return that list to user
        """
        return self.numbers

    def filter_values(self, filter_func: lambda x: x):
        """
        this method filter the list using lambda function

        filter_func : this argument return the filter formula for filter data

        return that filter data list to user
        """
        filtered_numbers = filter(filter_func, self.numbers)
        return list(filtered_numbers)

    def change_original_values(self, func: lambda x: x):
        """
        this method change original values the list using lambda function

        filter_func : this argument return the original values formula for data

        return that list to user
        """
        new_numbers = map(func, self.numbers)
        return list(new_numbers)

    def compound_the_numbers(self, reduce_func: lambda compound, d: compound + d):
        """
        this method compound the list using lambda function

        filter_func : this argument return the original values formula for data
        d: find compund interest formula
        
        return that list to user
        """
        # Use python reduce() here: terminal function that returns single value compounded
        compounded_value = reduce(reduce_func, self.numbers)
        return list(compounded_value)

    def sort(self):
        """
        this method sort the list using 
 
        return that sorted list to user
        """
        number_list = self.numbers
        for i in range(len(number_list)):
            index = i
            for j in range(i + 1, len(number_list)):
                if number_list[j] < number_list[index]:
                    index = j
                (number_list[i], number_list[index]) = (
                    number_list[index],
                    number_list[i],
                )
        return number_list


if __name__ == "__main__":
    numbers = [2, 5, 1, 66, 22, 11, 10]
    n1 = Number(numbers)
    lambda_func1 = lambda x: x + x
    lambda_func3 = lambda x, y: x + y
    print("Numbers: ", n1.get())
    print("New values: ", n1.change_original_values(func=lambda_func1))
    # print("Filtered values:", n1.filter_values(filter_func=lambda_func2))
    print("Compounded value:", n1.compound_the_numbers(reduce_func=lambda_func3))
    print("Sorted list:", n1.sort())
