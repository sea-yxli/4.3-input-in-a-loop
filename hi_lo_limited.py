import random
num = random.randint(1, 101)
count = 1
print(num)

print("I'm thinking of a number between 1-100. You have 7 guesses.")
guess = int(input(f"Guess {count}: ")) 


while guess != num and count < 7:
  if guess > num:
    print("Sorry, you are too high.")
    guess = int(input(f"Guess {count}: ")) 
    count += 1

    
  else:
    print("Sorry, you are too low.")
    guess = int(input(f"Guess {count}: "))
    count += 1

if count > 7:
  print("Sorry, you ran out of tries.")

else:
  print("Good job! You guessed the number.")
