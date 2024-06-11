__doc__ = """
Solution summary
We maintain track of two values using a slow pointer and a fast pointer. The slow runner advances one number at each step, while the fast runner advances two numbers. We detect if there is any cycle by comparing the two values and checking if the fast runner has indeed reached the number one. We return True or False depending on if those conditions are met.

Time complexity
The time complexity for this algorithm is 
𝑂(log𝑛), where 𝑛 is the input number.

The worst case time complexity of this algorithm is given by the case of a non-happy number, since it gets stuck in a cycle, whereas a happy number quickly converges to 
1. Let’s first calculate the time complexity of the Sum Digits function. Since we are calculating the sum of all digits in a number, the time complexity of this function is 𝑂(log⁡𝑛)O(log n), because the number of digits in the number 𝑛 is log⁡10 𝑛 log 10​ n.

To estimate the count of numbers in a cycle, let’s consider the following two cases:

Numbers with three digits: The largest three-digit number is 999. The sum of the squares of its digits is 
243. Therefore, for three-digit numbers, no number in the cycle can go beyond 243. Therefore, the time complexity in this case is given as 𝑂(243×3)O(243×3), where 243243 is the maximum count of numbers in a cycle and 33 is the number of digits in a three-digit number. This is why the time complexity in the case of numbers with three digits comes out to be 𝑂(1)O(1).Numbers with more than three digits: Any number with more than three digits will lose at least one digit at every step until it becomes a three-digit number. For example, the first four-digit number that we can get in the cycle is 10531053, which is the sum of the square of the digits in 99999999999999999999999999. Therefore, the time complexity of any number with more than three digits can be expressed as 𝑂(log⁡𝑛+log⁡log⁡𝑛+log⁡log⁡log⁡𝑛+…)O(logn+loglogn+logloglogn+…). Since 𝑂(log⁡𝑛)O(logn) is the dominating term, we can write the time complexity as 𝑂(log⁡𝑛)O(logn).

Therefore, the total time complexity comes out to be 𝑂(1+log⁡𝑛)O(1+logn), which is 𝑂(log⁡𝑛)O(logn).Space complexityThe space complexity for this algorithm is 𝑂(1)O(1).
"""
def is_happy_number(n):

    # Helper function that calculates the sum of squared digits.
    def sum_of_squared_digits(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        print("\t\tSum of squared digits: ", total_sum)
        return total_sum

    slow_pointer = n  # The slow pointer value
    print("\tSetting slow pointer = input number", slow_pointer)
    print("\tSetting fast pointer = sum of squared digits of ", n, sep="")
    fast_pointer = sum_of_squared_digits(n)  # The fast pointer value
    print("\tFast pointer:", fast_pointer)
    while fast_pointer != 1 and slow_pointer != fast_pointer:  # Terminating condition
        print("\n\tRepeatedly updating slow and fast pointers\n")
        # Incrementing the slow pointer by 1 iteration
        slow_pointer = sum_of_squared_digits(slow_pointer)
        print("\t\tThe updated slow pointer is", slow_pointer, "\n")
        # Incrementing the fast pointer by 2 iterations
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))
        print("\t\tThe updated fast pointer is ", fast_pointer, "\n")
    # If 1 is found then it returns True, otherwise False
    if(fast_pointer == 1):
        print("\tSince fast pointer has converged to 1, the input number is a happy number.\n")
        return True
    print("\tFast pointer has not converged to 1, the input number is not happy number.\n")
    return False


def main():
    inputs = [1, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print(i+1, ".\tInput Number: ", inputs[i], sep="")
        print("\tIs it a happy number? ", is_happy_number(inputs[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()