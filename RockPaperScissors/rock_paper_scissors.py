import random

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

print("What do you choose? Type")
print("0 for Rock")
print("1 for Paper")
print("2 for Scissors")

choice = int(input())
if choice < 0 or choice > 2:
    print("Invalid input, please run again!")
    exit(0)

index_list = [rock, paper, scissors]

print(index_list[choice])

computer_chose = random.randint(0, 2)

print("Computer chose: ")
print(index_list[computer_chose])

if choice == computer_chose:
    print("It's a draw!")
elif choice == 0:
    if computer_chose == 2:
        print("You won!")
    else:
        print("You lose!")
elif choice == 1:
    if computer_chose == 2:
        print("You lose!")
    else:
        print("You won!")
elif choice == 2:
    if computer_chose == 1:
        print("You lose!")
    else:
        print("You won!")
