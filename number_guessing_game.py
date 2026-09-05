import random
score = 100
hidden_number = random.randint(1 , 100)
print("Hidden Number",hidden_number)
for i in range(5):
    guess = int(input("Guess a nubmber: "))
    if guess == hidden_number:
        print("Congratulation you won!")
        print("score",score)
    elif guess > hidden_number:
        print("hint : your guess is too High!")
        score -=20
    else:
        print("hint : your guess is too low!")
        score -= 20
else:
    print("All chances are gone!")
    print("you lost!")
    
