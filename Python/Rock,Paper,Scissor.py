import random

def get_user_choice():
    choice = input("Enter (Rock, Paper, Scissors): ")
    while choice not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'.")
        choice = input("Enter 'Rock', 'Paper', 'Scissors'")
    return choice

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissor' and computer_choice == 'Paper'):
        if user_choice == 'Rock':
            return "Rock breaks the Scissors! You Win!"
        elif user_choice == 'Paper':
            return "Paper wraps the Rock! You Win!"
        else:
            return "Scissors cuts the Paper! You Win!"
    else:
        if computer_choice == 'Rock':
            return "Rock breaks the Scissors! Computer Wins!"
        elif computer_choice == 'Paper':
            return "Paper wraps the Rock! Computer Wins!"
        else:
            return "Scissors cuts the Paper! Computer Wins!"
        
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}, the computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if 'You' in result:
            user_score += 1
        elif 'Computer' in result:
            computer_score += 1
        play_again = input("Play again? (y/n): ")
        if play_again != 'y':
            break
    print("Final Scores:")
    print(f"Computer: {computer_score}")
    print(f"Player: {user_score}")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
