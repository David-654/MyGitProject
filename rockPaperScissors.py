computerChoice = "scissors"
user_choice = input("Do you want rock, paper or scissors?")

if computerChoice == user_choice:
    print ("Its a TIE")
elif user_choice == "rock" and computerChoice == "scissors":
    print("You win, computer loses :( ")
elif user_choice == "paper" and computerChoice == "rock":
    print("You win, computer loses :( ")
elif user_choice == "scissors" and computerChoice == "paper":
    print ("You win, computer loses :( ")
else:
    print ("You lose, computer wins :) ")
