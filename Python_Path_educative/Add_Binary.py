def add_binary(str1, str2):
  p1 = len(str1)-1
  p2 = len(str2)-1
  carry = 0
  res = ""
  for i in range(max(len(str1),len(str2))):
    bin_num1 = int(str1[p1]) if p1 >= 0 else 0
    bin_num2 = int(str2[p2]) if p2 >= 0 else 0
    bin_sum = (bin_num1 + bin_num2 + carry)
    
    if bin_sum == 1:
      carry = 0
      res += "1"
    elif bin_sum == 2:
        carry = 1
        res += "0"
    elif bin_sum == 3:
        carry = 1 
        res += "1"
    else:
        res += str(bin_sum)
        
    p1 -= 1
    p2 -= 1
    
  if carry == 1:
    res += str(carry)
  return res[::-1]
  


print(add_binary("101" , "1101")) 
# print(add_binary("1111" , "1011"))  #11010
# print(add_binary("101010" , "110110")) #1100000