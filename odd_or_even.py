
num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))
if num % check == 0:
    print("{} divides evenly by {}.".format(num, check))
else:
    print("{} does not divide evenly by {}.".format(num, check))
