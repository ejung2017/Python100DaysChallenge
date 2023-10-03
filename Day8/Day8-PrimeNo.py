def prime_number(number): 
    prime = True
    for i in range(2,number):
        if number%i==0: 
            prime = False 
    print(prime)

prime_number(11)
prime_number(27)

