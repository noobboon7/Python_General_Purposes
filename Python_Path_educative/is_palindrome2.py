# def is_palindrome(s):
#   start = 0
#   end = len(s) - 1
#   count = 0
#   while start <= end:
#     if count > 1:
#       return False
#     else:
#       if s[start] == s[end]:
#         start += 1
#         end -= 1
#       else:
#         if s[start+1] == s[end]:
#           start += 1
#         elif s[end-1] == s[start]:
#           end -= 1
#         count += 1
    
#   return True
def is_palindrome(s):
  start = 0
  end = len(s) - 1
  count = 0
  while start <= end:
    if count > 1:
      return False
    else:
      if s[start] == s[end]:
        start += 1
        end -= 1
      else:
        if valid_palindrome(s[start+1:end+1]):
          start += 1
        elif valid_palindrome(s[start:end]):
          end -= 1
        count += 1
    
  return True

def valid_palindrome(string):
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] == string[right]:
          left += 1
          right -= 1 
        else:
          return False
    return True
          

          
print(is_palindrome("abcdedadedecba")) #true