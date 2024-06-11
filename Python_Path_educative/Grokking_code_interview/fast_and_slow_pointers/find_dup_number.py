"""_summary_
Solution

We solve this problem using fast and slow pointers technique, without modifying the `nums` array and using only constant extra space.

For this problem, the duplicate number will create a cycle in the `nums` array. The cycle in the `nums` array helps identify the duplicate number.

To find the cycle, we’ll move in the `nums` array using the f(x)\=nums\[x\]f(x) = nums\[x\]f(x)\=nums\[x\] function, where xxx is the index of the array. This function constructs the following sequence to move:

x, nums\[x\], nums\[nums\[x\]\], nums\[nums\[nums\[x\]\]\], ...x, \\space nums\[x\], \\space nums\[nums\[x\]\], \\space nums\[nums\[nums\[x\]\]\], \\space ... x, nums\[x\], nums\[nums\[x\]\], nums\[nums\[nums\[x\]\]\], ...

In the sequence above, every new element is an element in `nums` present at the index of the previous element.

Let’s say we have an array, \[2, 3, 1, 3\]\[2, \\space 3,\\space 1,\\space 3\]\[2, 3, 1, 3\]. We’ll start with x\=nums\[0\]x=nums\[0\]x\=nums\[0\], which is 222, present at the 0th0^{th}0th index of the array and then move to nums\[x\]nums\[x\]nums\[x\], which is 111, present at the 2nd2^{nd}2nd index. Since we found 111 at the 2nd2^{nd}2nd index, we’ll move to the 1st1^{st}1st index, and so on. This example shows that if we’re given an array of length n+1n+1n+1, with values in the range \[1, n\]\[1,\\space n\]\[1, n\], we can use this traversal technique to visit all the locations in the array.

Time complexity#
The time complexity of the algorithm is 𝑂(𝑛), where 𝑛 is the length of nums. This is because, in each part of the solution, the slow pointer traverses nums just once.

Space complexity
The algorithm takes 𝑂(1) space complexity, since we only used constant space to store the fast and slow pointers.
"""
def find_duplicate(nums):
    # Initialize the fast and slow pointers and make them point the first
    # element of the array
    fast = slow = nums[0]
    # PART #1
    # Traverse in array until the intersection point is found
    while True:
        # Move the slow pointer using the nums[slow] flow
        slow = nums[slow]
        # Move the fast pointer two times fast as the slow pointer using the 
        # nums[nums[fast]] flow 
        fast = nums[nums[fast]]
        # Break the loop when slow pointer becomes equal to the fast pointer, i.e., 
        # if the intersection is found
        if slow == fast:
            break
    # PART #2
    # Make the slow pointer point the starting position of an array again, i.e.,
    # start the slow pointer from starting position
    slow = nums[0]
    # Traverse in the array until the slow pointer becomes equal to the
    # fast pointer
    while slow != fast:
        # Move the slow pointer using the nums[slow] flow
        slow = nums[slow]
        # Move the fast pointer slower than before, i.e., move the fast pointer
        # using the nums[fast] flow
        fast = nums[fast]
    # Return the fast pointer as it points the duplicate number of the array
    return fast

# Driver code
def main():
    nums = [
        [1, 3, 2, 3, 5, 4], 
        [2, 4, 5, 4, 1, 3], 
        [1, 6, 3, 5, 1, 2, 7, 4], 
        [1, 2, 2, 4, 3], 
        [3, 1, 3, 5, 6, 4, 2]
    ]
    for i in range(len(nums)):
        print(i + 1, ".\tnums = ", nums[i], sep="")
        print("\tDuplicate number = ", find_duplicate(nums[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
    