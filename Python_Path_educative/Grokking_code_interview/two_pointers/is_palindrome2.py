def is_palindrome(s):
  print("Input string: ", s)
  start = 0
  end = len(s) - 1
  count = 0
  while start <= end:
    print("Start: ", start, "End: ", end, "Count: ", count)
    if count > 1:
      print("Returning False")
      return False
    else:
      if s[start] == s[end]:
        start += 1
        end -= 1
        print("Characters matched. Start: ", start, "End: ", end)
      else:
        print("Characters did not match. Trying to find palindrome substring from Start: ", start+1, "to End: ", end+1)
        if valid_palindrome(s[start+1:end+1]):
          start += 1
          print("Palindrome found from Start: ", start, "to End: ", end+1)
        elif valid_palindrome(s[start:end]):
          end -= 1
          print("Palindrome found from Start: ", start, "to End: ", end)
        count += 1
    print()
  print("Returning True")
  return True

def valid_palindrome(string):
    print("String: ", string)
    print("Length of string: ", len(string))
    left = 0
    right = len(string) - 1
    while left <= right:
        print("Left: ", left, "Right: ", right)
        print("Character at left: ", string[left])
        print("Character at right: ", string[right])
        if string[left] == string[right]:
          print("Characters match")
          left += 1
          right -= 1 
        else:
          print("Characters do not match")
          return False
    print("Left pointer is greater than right pointer")
    return True
          
       
def main():
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR", "abcdedadedecba"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("\nIs it a palindrome?.....", is_palindrome(test_cases[i]))
        print("-" * 100)

if __name__ == '__main__':
    main()
