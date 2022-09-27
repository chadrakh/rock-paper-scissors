import random

while True:
    actions = ["rock", "paper", "scissors", "lizard", "spock"]

    computer_action = random.choice(actions)
    player_action = None

    while player_action not in actions:
        player_action = input("Choose! Rock, Paper, Scissors, Lizard or Spock?:").lower()

    if player_action == computer_action:
        print("Computer: ", computer_action)
        print("Player: ", player_action)
        print("It's a tie!")
    elif player_action == "rock":
        if computer_action == "paper":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Paper covers rock. You lose..")
        if computer_action == "scissors":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Rock crushes scissors. You win!")
        if computer_action == "lizard":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Rock crushes scissors. You win!")
        if computer_action == "spock":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Spock vaporises rock. You lose..")


    elif player_action == "paper":
        if computer_action == "rock":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Paper covers rock. You win!")
        if computer_action == "scissors":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Scissors cuts paper. You lose..")
        if computer_action == "lizard":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Lizard eats paper. You lose..")
        if computer_action == "spock":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Paper disproves Spock. You win!")


    elif player_action == "scissors":
        if computer_action == "rock":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Rock smashes scissors. You lose..")
        if computer_action == "paper":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Scissors cuts paper. You win!")
        if computer_action == "lizard":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Scissors decapitates lizard. You win!")
        if computer_action == "spock":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Spock smashes scissors. You win!")


    elif player_action == "lizard":
        if computer_action == "rock":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Rock crushes lizard. You lose..")
        if computer_action == "paper":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Lizard eats paper. You lose..")
        if computer_action == "scissors":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Scissors decapitates lizard. You lose..")
        if computer_action == "spock":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Lizard poisons Spock. You win!")


    elif player_action == "spock":
        if computer_action == "rock":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Spock vaporises rock. You win!")
        if computer_action == "paper":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Paper disproves Spock. You lose..")
        if computer_action == "scissors":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Spock smashes scissors. You win!")
        if computer_action == "lizard":
            print("Computer: ", computer_action)
            print("Player: ", player_action)
            print("Lizard poisons Spock. You lose..")
    
    play_again = input("Would you like to play again? (y/n): ").lower()

    if play_again != "y":
        break

print("Thanks for playing, bye bye!")

# switch case > if
# add ui