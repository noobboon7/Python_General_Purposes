"""Solution summary
First, sort the array in ascending order. To find a triplet whose sum is equal to the target value, loop through the entire array. In each iteration:

1. Store the current array element and set up two pointers (low and high) to find the other two elements that complete the required triplet.

  - The low pointer is set to the current loop’s index + 1.

  - The high is set to the last index of the array.

2. Calculate the sum of array elements pointed to by the current loop’s index and the low and high pointers.

3. If the sum is equal to target, return TRUE.

4. If the sum is less than target, move the low pointer forward.

5. If the sum is greater than target, move the high pointer backward.

Repeat until the loop has processed the entire array. If, after processing the entire array, we don't find any triplet that matches our requirement, we return FALSE.

Time complexity
In the solution above, sorting the array takes O(nlog(n)) and the nested loop takes O(n2) to find the triplet. Here, is the number of elements in the input array. Therefore, the total time complexity of this solution is O(nlog(n)+n2)
, which simplifies to O(n2).

Space complexity
The space complexity of this solution can range from O(log(n)) to O(n), as per the sorting algorithm we use. We use the built-in Python function, sort(), so the space complexity of the provided solution is O(n).
"""
def find_sum_of_three(nums, target):
    # Sort the input list
    nums.sort()

    # Fix one integer at a time and find the other two
    for i in range(0, len(nums)-2):
        # Initialize the two pointers
        low = i + 1
        high = len(nums) - 1

        # Traverse the list to find the triplet whose sum equals the target
        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            # The sum of the triplet equals the target
            if triplet == target:
                return True
                
            # The sum of the triplet is less than target, so move the low pointer forward
            elif triplet < target:
                low += 1
            
            # The sum of the triplet is greater than target, so move the high pointer backward
            else:
                high -= 1
    
    # No such triplet found whose sum equals the given target
    return False

# Driver code
def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

if __name__ == '__main__':
    main()