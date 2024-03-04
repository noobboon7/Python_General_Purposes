# sums on positive integers
def sum_digits(num):
    sum = 0
    if num == 0:
        return sum
    else:
        while(num != 0):
            sum += num%10
            num //= 10

    return sum

print(sum_digits(123))