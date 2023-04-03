import random
num = random.randint(1, 11)
tries = 0

print("I have chosen a number between 1 and 10. Try to guess it.")
guess = int(input("Your guess: "))
tries += 1

while guess != num:
  print("That is incorrect. Guess again.")
  guess = int(input("Your guess: "))
  tries += 1

print("That's right! You're a good guesser.")
print(f"It only took you {tries} tries!")
