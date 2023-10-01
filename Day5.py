student_heights = input("Input the heights: ").split()
for height in range(0, len(student_heights)): 
    student_heights[height] = int(student_heights[height])
print(student_heights)

#functions 
len(student_heights) #length 
sum(student_heights) 

#calculate the average
students = 0
sum = 0
for height in range(0, len(student_heights)): 
    students+=1 
    sum+=student_heights[height]
    avg = sum/students 

print("Average score: ", avg)

#find the max and min
max = 0 
min = student_heights[0]
for height in range(0, len(student_heights)): 
    if height > max: 
        max = student_heights[height] 
    if min > height: 
        min = student_heights[height] 
print(f"Maximum: {max}, Minimum: {min}")

#range(a, b, c) -> [a, b) with c increments 

#FizzBuzz interview Q 
#multiples of 3 = Fizz, multiples of 5 = Buzz, multiples of both = FizzBuzz
for i in range(1,101): 
    if i%3==0 and i%5!=0: 
        print("Fizz")
    elif i%3!=0 and i%5==0: 
        print("Buzz")
    elif i%3==0 and i%5==0: 
        print("FizzBuzz")
    else: 
        print(i)

#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#easy level
# in order 
print("Easy version: ")
for i in range(0,nr_letter): 
    print(random.choice(letters), end="")
for i in range(0, nr_numbers): 
    print(random.choice(numbers), end="")
for i in range(0, nr_symbols): 
    print(random.choice(symbols), end="")
print()

#hard level
# totally random 
print("Hard version: ")
list1 = [] 
for i in range(0,nr_letter): 
    list1.append(random.choice(letters))
for i in range(0, nr_numbers): 
    list1.append(random.choice(numbers))
for i in range(0, nr_symbols): 
    list1.append(random.choice(symbols))
random.shuffle(list1)
for i in range(0,len(list1)): 
    print(list1[i], end="")