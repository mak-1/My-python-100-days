rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player = input("Chose between: rock, paper or scissor: ").lower()

scelta_pc_numerica = random.randint(0,2)


lista_scelta= [rock,paper,scissors]
lista_mosse=["rock","paper","scissors"]
pc = lista_mosse[scelta_pc_numerica]

################################
if player =="rock":
  player_mossa=0
elif player == "scissors":
  player_mossa=2
else:
  player_mossa = 1

#########################
if pc =="rock":
  pc_mossa=0
elif pc == "scissors":
  pc_mossa=2
else:
  pc_mossa = 1

print(f"Your choiche:\n {player} \n {lista_scelta[player_mossa]}")
print(f"PC chosees:\n {pc} \n {lista_scelta[pc_mossa]}")

if player == "rock" and pc == "scissors":
  print("You win")
elif player == "scissors" and pc == "rock":
  print("You lose")
elif player== "scissors" and pc == "paper":
  print("You win")
elif player== "paper" and pc == "scissors":
  print("You lose")
elif player == "paper" and pc == "rock":
  print("You win")
elif player == "rock" and pc == "paper":
  print("You lose")
else:
  print("Draw")