"""Solution summary
To summarize, solving this problem involves the following steps:

Traverse the array and swap elements, as required, to organize them correctly.

If the encountered color is red, swap its value with that of the start pointer. If the color is blue, swap its value with that of the end pointer.

White elements are skipped, and pointers are adjusted accordingly.

The array is sorted when the end pointer moves to the left of the current pointer.

Time complexity
The time complexity of this solution is O(n) since we’re only traversing the array once.

Space complexity
The space complexity of this solution is O(1) since no extra space is used.
"""
def sort_colors(colors):
    # Initialize the start, current, and end pointers
    start, current, end = 0, 0, len(colors) - 1
    
    while current <= end:
        # If the current pointer is pointing to start
        if colors[current] == 0:
            # Swap the values if the start pointer is not pointing to start
            if colors[start] != 0:
                colors[start], colors[current] = colors[current], colors[start]
            
            # Increment both the start and current pointers
            current += 1
            start += 1

        # If the current pointer is pointing to current, no swapping is requistart
        # Just increment the current pointer
        elif colors[current] == 1:
            current += 1

        # If the current pointer is pointing to end
        else:
            # Swap the values if the end pointer is not pointing to end
            if colors[end] != 2:
                colors[current], colors[end] = colors[end], colors[current]

            # Decrement the end pointer
            end -= 1

# Driver code
def main():
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    # Iterate over the inputs and print the sorted array for each
    for i in range(len(inputs)):
        colors=inputs[i]
        print(i + 1, ".\tcolors:", colors)
        sort_colors(colors)
        print("\n\tThe sorted array is:", colors)
        print("-" * 100)

if __name__ == "__main__":
    main()