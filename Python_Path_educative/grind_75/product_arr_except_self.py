"""Solution summary
The solution can be summarized in the following steps:

Create a list with the same length as the input list, initialized with 
1
1
s.

Keep track of products on the left and right sides of the current element.

Use two pointers—one starting from the beginning and the other from the end of the list.

Multiply and update values in the output array based on accumulated products and current element values.

Move the pointers toward each other to process the entire list.

Time complexity
The time complexity of this solution is O(n), since both the pointers simultaneously traverse the length of the array once.

Space complexity
The space complexity of this solution is O(1), since it doesn’t use any additional array for computations but only constant additional space.
  """
def product_except_self(nums):
    # Get the length of the input list
    n = len(nums)
    
    # Initialize a result list with 1's for products
    res = [1] * n
    
    # Initialize variables for left and right products
    left_product, right_product = 1, 1
    
    # Initialize pointers for the left and right ends of the list
    l = 0
    r = n - 1

    # Iterate through the list while moving the pointers towards each other
    while l < n and r > -1:
        # Update the result at the left index with the accumulated left product
        res[l] *= left_product

        # Update the result at the right index with the accumulated right product
        res[r] *= right_product
        
        # Update the left product with the current element's value
        left_product *= nums[l]

        # Update the right product with the current element's value
        right_product *= nums[r]
        
        # Move the left pointer to the right
        l += 1
        
        # Move the right pointer to the left
        r -= 1

    # Return the final product result list
    return res

# Driver code
def main():
    
    inputList = [[1, 5, 10], [3, 5, 0, -3, 1], [7, 8, 9, 10, 11], [2, -4, -8, -11, 11], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5]]
    
    # For each input, print the input and its maximum depth
    for i in range(len(inputList)):
        print (str(i + 1) + '.\tnums:', inputList[i])
        print ('\tres:', product_except_self(inputList[i]))
        print ('-' * 100)

if __name__ == '__main__':
    main()