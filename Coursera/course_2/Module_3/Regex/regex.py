import re
def repeating_letter_a(text):
  result = re.search(r"[A|a].*[A|a]", text)
  return result
  # return result != None << original code 
# commented booleans are testcase given
print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True