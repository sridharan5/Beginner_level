import logo
import random
start = True
while start:
    print(logo.logo)
    logo.content_printing()
    level = input("Choose difficulty . Type 'easy' or 'hard': ").lower()
    guessed_number = random.randint(1, 100)
    if level == 'easy':
        count = 11
        for i in range(1, count):
            print(f"You have {count-i} attempts remaining to guess the number.")
            user_guesses = int(input("Make a guess: "))
            if user_guesses < guessed_number:
                logo.low()
            elif user_guesses > guessed_number:
                logo.high()
            else:
                break
    elif level == 'hard':
        count = 6
        for i in range(1, count):
            print(f"You have {count-i} attempts remaining to guess the number.")
            user_guesses = int(input("Make a guess: "))
            if user_guesses < guessed_number:
                logo.low()
            elif user_guesses > guessed_number:
                logo.high()
            elif user_guesses == guessed_number:
                logo.win()
                break
    else:
        print("Please check your input. Type valid option 'easy' or 'hard'. ")
    if user_guesses == guessed_number:
        logo.win()
    else:
        print(f"Guessed number is {guessed_number}  😁 ")
        logo.loose()
    play = input("Do you want to play again ? Type 'yes' to restart the Game or 'no' to exit the game. ").lower()
    if play == 'yes':
        start = True
    elif play == 'no':
        start = False
    else:
        print("You give a invalid input..")
        print("Game over ....")