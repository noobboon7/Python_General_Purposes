import re 


print('don\'t maths, we got you')
print("Type 'quit' to exit")

previous = 0 
run = True

def performMath():
  global run
  global previous

  equation = ''
  try: 
    if previous == 0:
      equation = input('Enter equation:')
    else: 
      equation = input(str(previous))

    if equation == 'quit':
      print('Bye Felicia!')
      run = False
    else:
      # this regex is to prevent pyhton code from running on the calc
      equation = re.sub('[a-zA-Z,.:()" "]', '', equation) 

      if previous == 0:
        previous = eval(equation)
      else:
        previous = eval(str(previous) + equation)
  except:
    print('that not an equation, try: 1+1, etc.')

while run: 
  performMath()
