import random
Choose = ["Rock","paper","scissor"]
from_computer = random.choice(Choose)
print(from_computer)
i = 0
while i < 5:
    My_choice = input("Enter your choice: ")
    print(My_choice)
    if My_choice == from_computer:
        print("Its a Draw")
    elif My_choice == "Rock" and from_computer == "Paper":
        print("Computer Wins")
    elif My_choice == "Rock" and from_computer == "scissor":
        print("You win")
    elif My_choice == "scissor" and from_computer == "Paper":
        print("You Win")
    elif My_choice == "scissor" and from_computer == "Rock":
        print("Computer Wins")
    elif My_choice == "paper" and from_computer == "Rock":
        print("You Win")
    elif My_choice == "paper" and from_computer == "scissor":
        print("Computer Wins")

