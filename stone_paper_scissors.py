
print("This is 'Stone Paper Scissors' game.")
answers = ["Stone", "Paper", "Scissors"]

stop = False
while not stop:
    decision_1 = input("Player's 1 decision (Stone Paper Scissors): ")
    decision_2 = input("Player's 2 decision (Stone Paper Scissors): ")

    if decision_1 not in answers or decision_2 not in answers:
        print("Error! Check your decisions")
    elif decision_1 == decision_2:
        print("Draw!")
    elif decision_1 == "Stone" and decision_2 == "Paper":
        print("Player 2 wins the game!")
    elif decision_1 == "Stone" and decision_2 == "Scissors":
        print("Player 1 wins the game!")
    elif decision_1 == "Paper" and decision_2 == "Stone":
        print("Player 1 wins the game!")
    elif decision_1 == "Paper" and decision_2 == "Scissors":
        print("Player 2 wins the game!")
    elif decision_1 == "Scissors" and decision_2 == "Stone":
        print("Player 2 wins the game!")
    elif decision_1 == "Scissors" and decision_2 == "Paper":
        print("Player 1 wins the game!")

    choice = input("If you want to play one more time press 'y': ")
    if choice != "y":
        stop = True
