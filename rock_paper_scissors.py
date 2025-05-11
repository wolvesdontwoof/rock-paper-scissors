import random

def get_user_choice():
    print("\nChoices: rock, paper, scissors")
    user = input("Enter your choice: ").lower()
    while user not in ['rock', 'paper', 'scissors']:
        user = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return user

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")
        print(determine_winner(user_choice, comp_choice))

        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play()
