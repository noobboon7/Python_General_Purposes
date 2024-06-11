# How to set up two pointers in an array

def two_pointers(array):
    left = 0
    right = len(array) - 1
    while left <= right:
        print(f"left: {array[left]}, right: {array[right]}")
        left = left + 1
        right = right - 1
        print(f"new left: {array[left]}, new right: {array[right]}")
    