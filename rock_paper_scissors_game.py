import random

options = ["rock", "paper", "scissors"]
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in ["r", "p", "s"]:
        player = input("Enter a choice (r for rock, p for paper, s for scissors): ").lower()

    if player == "r":
        player = "rock"
    elif player == "p":
        player = "paper"
    elif player == "s":
        player = "scissors"

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        running = True
    elif play_again == "n":
        running = False
    else:
        raise SystemExit("Invalid Input. Try again...")

print("Thanks for playing!")
