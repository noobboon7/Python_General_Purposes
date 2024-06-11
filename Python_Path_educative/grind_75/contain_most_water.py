"""Solution summary
1. Initialize two pointers, start and end, at the beginning and end of the input array, respectively.

2. Iterate through the array until the pointers converge.

3.In each iteration, perform the following steps:

  - Calculate the distance, width, between the two vertical lines pointed by the start and end pointers.

  - Multiply the height of the shorter vertical line with the width to calculate the area. Also, update the value of the maximum area.

  - Move the pointer pointing to the shorter vertical line inward by one step.

4. After iterating through the array, return the maximum area calculated.

Time complexity
The time complexity of this solution is O(n), where n is the length of the input array since we have visited the elements of the input array only once.

Space complexity
The space complexity of this solution is O(1), since we have only used constant space.
"""
def container_with_most_water(height):
    # Initialize max area as zero and the start and end pointers to the two ends
    # of the array
    max_area = 0 
    start = 0
    end = len(height) - 1
    
    while start < end:
        # Calculate the width between the lines
        width = end - start
        # Calculate the max area using the shortest height and the
        # distance between the two lines
        max_area = max(max_area, min(height[start], height[end]) * (width))
        
        # Move the start if it has the shorter height
        if height[start] <= height[end]:
            start+=1
        # Otherwise move the end
        else:
            end-=1

    # Return the maximum area
    return max_area

# Driver code
def main():
    heights = [
                [1, 8, 6, 2, 5, 4, 8, 3, 7], 
                [20, 30, 9, 69],
                [13, 18, 12, 8],
                [45, 32, 56, 99], [23, 20]
                ]
    index = 1
    for i in heights:
        print(str(index)+".\tHeights: "+str(i))
        print("\n\tMaximum Area: " + str(container_with_most_water(i)))
        index += 1
        print("-" * 100)


if __name__ == "__main__":
    main()