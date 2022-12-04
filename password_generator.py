#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&Pnr
lettere_Scelte =[]
#print(random.randint()
for n in range(1,nr_letters+1):
  lettere_Scelte.append(letters[random.randint(0,nr_letters)])

simboli_scelti = []
for n in range(1,nr_symbols+1):
  simboli_scelti.append(symbols[random.randint(0,nr_symbols)])

numeri_scelti = []
for n in range(1,nr_numbers+1):
  numeri_scelti.append(numbers[random.randint(0,nr_numbers)])

lettere_Scelte.extend(simboli_scelti)
lettere_Scelte.extend(numeri_scelti)
print(lettere_Scelte)
password=''
for s in range(0,len(lettere_Scelte)):
  password+=str(lettere_Scelte.pop(random.randint(0,len(lettere_Scelte)-1)))
print(password)
  