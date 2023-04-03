#How is a while loop similar to an if statement?
  #they both only execute code (the lines that are indented below it) if a certain condition is met
# How is a while loop different from an if statement?
  #a while loop is a loop, meaning that as long as the condition is met, it is going to continuously execute the code until the condition is no longer met and it breaks out of the loop. An if statement will be only checked once. 
# What would we have to change in our program if the PIN was stored as an integer rather than a string? For example if it was initialized as PIN = 12345.
  #we would need to add int before input to convert the string into an integer
# Comment out the line entry = input(...) from inside the while loop. What happens? Why?
  #the code prints out "INCORRECT PIN. TRY AGAIN." indefinitely because it is stuck inside the while loop and the user does not have the opportunity to enter a new pin. 
# (Uncomment the entry = input(...) before you turn in the assignment.)

PIN = 12345

print("WELCOME TO THE BANK OF GALLO.")
entry = int(input("ENTER YOUR PIN: "))

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = int(input("ENTER YOUR PIN: "))


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
