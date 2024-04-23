"""_summary_
Time complexity
The time complexity of this solution is O(n), where n is the length of the input string s. This is because we iterate through the input string once, character by character, without nested loops or recursive calls.

Space complexity
The space complexity of this solution is O(1).
"""
def myAtoi(s):

    # To store the final integer result
    result = 0

    # To store the sign which would determine whether the result should be positive (1) or negative (-1)
    sign = 1

    # Index for iterating through the string
    i = 0

    # Ignore any leading whitespaces
    while i < len(s) and s[i] == ' ':
        i += 1
    
    # Check for sign
    if i < len(s) and (s[i] == '-' or s[i] == '+'):

        # Set sign to negative if a minus sign is found
        if s[i] == '-':
            sign = -1 
        # Then, move to the next character
        i += 1
    
    # Read the digits
    while i < len(s) and '0' <= s[i] <= '9':

        # Convert the current character to an integer
        digit = ord(s[i]) - ord('0')

        # Check for overflow
        if result > (2**31 - 1 - digit) // 10:

            # If there's an overflow, return the maximum or minimum 32-bit integer value
            return sign * (2**31 - 1) if sign == 1 else sign * (2**31)
        
        # Update the result by multiplying it by 10 and adding the current digit
        result = result * 10 + digit

        # Move to the next character
        i += 1
    
    # Return the final result, adjusted for the sign
    return sign * result

# Driver code
def main():
    input_strings = ["25", "   -25", "999 with words", "words and 567", "-91283472332", "91283472332"]
  
    for i in range(len(input_strings)):
        print(i+1, ".\tInput string     : ", end="")
        print('"{0}"'.format(input_strings[i]))
        
        stoi = myAtoi(input_strings[i])
        
        print("\tConverted integer: ", stoi)
        print("-" * 100)

if __name__ == '__main__':
  main()