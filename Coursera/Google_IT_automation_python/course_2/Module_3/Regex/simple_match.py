import re
"""Regex examples
  
r”\d{3}-\d{3}-\d{4}”  This line of code matches U.S. phone numbers in the format 111-222-3333.


r”^-?\d*(\.\d+)?$”  This line of code matches any positive or negative number, with or without decimal places.


r”/^(.+)/([^/]+)$/” This line of code matches any path and filename.
  """

result = re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazaar")
print(result)


print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

print('\n')
print('*'*300)
print('\n')


# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.

def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text)
  return result
  # return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


print('\n')
print('*'*300)
print('\n')

print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^ A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

print('\n')
print('*'*300)
print('\n')

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))


print('\n')
print('*'*300)
print('\n')

# Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s]+[.?!]$", text)
  return result
  # return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

print('\n')
print('*'*300)
print('\n')

def check_web_address(text):
  pattern = r"[www.]?\w+[.][a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

print('\n')
print('*'*300)
print('\n')


def check_time(text):
  pattern = r"[0-9]?[0-9]:[0-5][0-9](\s?[aApP][mM])"
  result = re.search(pattern, text)
  return result 
  # return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

print('\n')
print('*'*300)
print('\n')


def contains_acronym(text):
  pattern = r"\(\w{2,10}\)" 
  result = re.search(pattern, text)
  return result 
  # return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

print('\n')
print('*'*300)
print('\n')

def correct_function(text):
  result = re.search(r"\s+[0-9]{5}(-[0-9]{4})?", text)  # Corrected regex pattern with space
  return result 
  # return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False