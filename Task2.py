#Task 1: check if a number is even or odd using if-else statement

num =int(input("Enter a number: "))
print ("method 1: using if-else statement:\n")
if num%2 ==0:
    print("The number", num, "is  even.")
else:
    print("The number", num, "is odd.")

print("\n")
print ("method 2: using ternary operator:\n")
print("Entered Number is even.", num) if num%2==0 else print ("Entered Number is odd.", num) 





