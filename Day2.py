#Tip Calculator
print("What was the total bill?")
total = float(input())
print("How many people to split the bill?")
n = float(input())
print("What percentage tip would you like to give?")
tip_percent = float(input())*0.01+1

pay = (total / n) * (tip_percent) #/ : divide //: floor division
print("Each person should pay: $" + str(pay))

#fstring = function string 
score = 0
height = 1.8 
isWinning = True

print(f"your score is {score}, your height is {height}, and are you winning? {isWinning}")

age = int(input("What's your current age?"))
months = (90-age)*12
weeks = (90-age)*52
days = (90-age)*365
print(f"You have {days} days, {weeks} weeks, and {months} months left.")