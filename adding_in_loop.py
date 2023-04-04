total = 0
print("I will add up the numbers you give me.")
number = int(input("Number: "))

while number != 0:
  total += number
  number = int(input("Number: "))
print(f"The total is {total}.")
