import random 

def guess():
  random_num = random.randint(1,10)
  guess = 0
  
  while guess != random_num: 
    guess = int(input('Guess a number between 1 and 10: '))
    if(guess < random_num):
      print("Your guess is too low, Try again")
    elif guess > random_num:
        print("Your guess is to high, Try again")
        
  print("WOOT! you got it! You win nothing. now get outta hea! EH!")

guess()

