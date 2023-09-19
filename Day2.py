#Tip Calculator
print("What was the total bill?")
total = float(input())
print("How many people to split the bill?")
n = float(input())
print("What percentage tip would you like to give?")
tip_percent = float(input())*0.01+1

pay = (total // n) * (tip_percent)
print("Each person should pay: $" + str(pay))