# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1_lower = name1.lower()
name2_lower = name2.lower()
count  = 0
count2 = 0
count += name1_lower.count("t")
count += name1_lower.count("r")
count += name1_lower.count("u")
count += name1_lower.count("e")
count += name2_lower.count("t")
count += name2_lower.count("r")
count += name2_lower.count("u")
count += name2_lower.count("e")

count2 += name1_lower.count("l")
count2 += name1_lower.count("o")
count2 += name1_lower.count("v")
count2 += name1_lower.count("e")
count2 += name2_lower.count("l")
count2 += name2_lower.count("o")
count2 += name2_lower.count("v")
count2 += name2_lower.count("e")
score = str(count)+ str(count2)
score =int(score)
if score < 10 or score >90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
