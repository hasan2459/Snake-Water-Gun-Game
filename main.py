import random
print("Welcome to snake water gun game")

choices = ["snake", "water", "gun"]

player_score = 0
computer_score = 0

while True:

    player = input("Enter snake, water, gun or quit: ").lower()

    if player == "quit":
        print("\nThanks for playing!")
        print(f"you: {player_score}")
        print(f"computer: {computer_score}")
        print(f"final score: you {player_score} - computer {computer_score}")
        break


    if player not in choices:
        print("invalid choice! please enter snake, water, gun or quit.")
        continue

    computer = random.choice(choices)
    print(f"computer choice: {computer}")

    if player == computer:
        print("it's a draw!")
    elif player == "snake" and computer == "water":
        print("You win!")
        player_score += 1
    elif player == "water" and computer == "gun":
        print("You win!")
        player_score +=1
    elif player == "gun" and computer == "snake":
        print("You win!")
        player_score +=1
    else :
        print("computer wins!")
        computer_score += 1

    print (f"score: You {player_score} - computer {computer_score}")

