import random
print("HERE COMES THE DICE!")

dice1 = random.randint(1, 7)
print(f"Roll one: {dice1}")
dice2 = random.randint(1, 7)
print(f"Roll two: {dice2}")
total = dice1 + dice2
print(f"The total is {total}")

while dice1 != dice2:
  dice1 = random.randint(1, 7)
  print(f"Roll one: {dice1}")
  dice2 = random.randint(1, 7)
  print(f"Roll two: {dice2}")
  total = dice1 + dice2
  print(f"The total is {total}")

