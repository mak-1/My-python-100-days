#Write your code below this line 👇
import math
def prime_checker(number):
    # Program to check if a number is prime or not
    

    # To take input from the user
    #number = int(input("Enter a number: "))

    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if number > 1:
        # check for factors
        for i in range(2,math.floor(math.sqrt(number)+1)):
            if (number % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")




#Write your code above this line 👆
        
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)