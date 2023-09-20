#leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0: 
    if year % 4 == 0: 
        if year % 400 == 0: 
            print("Leap year")
        else: 
            print("Not Leap")
    else: 
        print("Leap year")
else: 
    print("Not Leap")

#rock scissor or paper
import random
computer = random.randint(0,2)
user = int(input("Rock(0), Scissor(1), or Paper(2): "))
rps = ["Rock", "Scissor", "Paper"]

print(f"computer: {rps[computer]}  user: {rps[user]}")
if computer == user: 
    print("Draw")
elif computer > user: 
    print("user won")
else:
    print("computer won")