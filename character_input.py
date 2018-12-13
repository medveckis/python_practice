
import datetime as dt

name = input("Give me your name: ")
age = int(input("Give me your age: "))
number_of_times = int(input("Enter number of times to repeat the message: "))
year = dt.datetime.now().year + (100 - age)
print(number_of_times * "Hello, {}, there will be {} when you turn 100 years old.\n".format(name, year))
