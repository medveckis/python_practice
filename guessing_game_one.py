
import random as rnd

print("This game generates an integer number and you need to guess it!")

stop = False
counter = 0
while not stop:
    input_number = int(input("Enter a number: "))
    generated_num = rnd.randint(1, 9)

    if input_number != generated_num:
        while input_number != generated_num:
            if input_number > generated_num:
                print("Your number is higher than the actual! Try again.")
            elif input_number < generated_num:
                print("Your number is lower than the actual! Try again.")
            choice = input("If you want to give up on this try type 'give up': ")
            if choice == "give up":
                break
            else:
                input_number = int(input("Enter a number: "))

    if input_number == generated_num:
        print("You are correct, guessed number was {}.".format(generated_num))
        counter += 1

    choice = input("If you want to exit type 'exit': ")
    if choice == "exit":
        stop = True

print("Your score is {}. Good bye!".format(counter))
