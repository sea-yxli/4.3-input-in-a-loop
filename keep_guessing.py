import random
num = random.randint(1, 11)

print("I have chosen a number between 1 and 10. Try to guess it.")
guess = int(input("Your guess: "))

while guess != num:
  print("That is incorrect. Guess again.")
  guess = int(input("Your guess: "))

print("That's right! You're a good guesser.")
