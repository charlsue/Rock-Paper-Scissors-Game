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
while True:
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    if user_choice == "0":
        print(rock)
    elif user_choice == "1":
        print(paper)
    elif user_choice == "2":
        print(scissors)
    else:
        print("You typed an invalid number, you lose!")
    import random
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("Computer chose:")
        print(rock)
    elif computer_choice == 1:
        print("Computer chose:")
        print(paper)
    else:
        print("Computer chose:")
        print(scissors)

    rules = {
        ("0", "0"): "It's a draw",
        ("0", "1"): "You lose",
        ("0", "2"): "You win",
        ("1", "0"): "You win",
        ("1", "1"): "It's a draw",
        ("1", "2"): "You lose",
        ("2", "0"): "You lose",
        ("2", "1"): "You win",
        ("2", "2"): "It's a draw",
    }
    result = rules[(user_choice, str(computer_choice))]
    print(result)
    print("\n\n")
    print("Would you like to play again? Y/N")
    play_again = input().lower()
    if play_again == "y":
        continue
    else:
        break