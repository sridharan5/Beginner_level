import random

logo = """
  ___   ___   ___   ___   ___ 
 |A  | |K  | |Q  | |J  | |10 |
 |(`)| |(`)| |(`)| |(`)| |(`)|
 |_\_| |_\_| |_\_| |_\_| |_\_|
  ___   ___   ___   ___   ___   ___ 
 |A  | |2  | |3  | |4  | |5  | |6  |
 | /\| | /\| | /\| | /\| | /\| | /\|
 |_\/| |_\/| |_\/| |_\/| |_\/| |_\/|
  ___   ___   ___   ___   ___   ___   ___
 |A  | |2  | |3  | |4  | |5  | |6  | |7  |
 | ^ | | ^ | | ^ | | ^ | | ^ | | ^ | | ^ |
 |(,)| |(,)| |(,)| |(,)| |(,)| |(,)| |(,)|     ejm
  ___   ___   ___   ___  
 |A  | |K  | |Q  | |J  | 
 | O | | O | | O | | O | 
 |O,O| |O,O| |O,O| |O,O| etc. etc.            
  ___
 |JOK|
 |^%<|
 |___| 

"""


def start():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = []
    computer = []
    win_score = 21
    limit = 17
    loop_run = True
    loop = True
    running = True
    # Taking two cards for sample
    for i in range(2):
        taking_cards = random.choice(cards)
        computer.append(taking_cards)
    for i in range(2):
        taking_cards = random.choice(cards)
        user.append(taking_cards)
    # printing cards to the screen
    print(logo)
    print(f"User cards    : {user}")
    print(f"Computer's first cards '{computer[0]}' another card is hidden ")
    adding_score_for_computer = 0
    adding_score_for_user = 0
    # computer and user ace value changer
    if computer[0] == 11 and computer[1] == 11:
        computer[1] = 1
    if user[0] == 11 and user[1] == 11:
        user[1] = 1
    # adding two scores
    for i in computer:
        adding_score_for_computer += i
    for i in user:
        adding_score_for_user += i
    if adding_score_for_computer == win_score and adding_score_for_user == win_score:
        print(f"{user}and{computer}")
        print("Game draw")
        exit()
    elif adding_score_for_user >= win_score:
        print("Computer win -----")
    elif adding_score_for_computer >= win_score:
        print("User win -----")
    else:
        print(f"Your score is: {adding_score_for_user}")
        while loop:
            if adding_score_for_computer == adding_score_for_user:
                print(f"computer: {adding_score_for_computer} user: {adding_score_for_user}")
                print("Game draw .")
            while loop_run:
                if running:
                    option_for_user = input("User press 'y' to hit or press 'n' for hold ? ").lower()
                    if option_for_user == 'y':
                        dice_user = random.choice(cards)
                        print(f"You card value is : {dice_user}")
                        if dice_user == 11:
                            print("You taken ace card , The card value will be change depends on your score")
                            check_user = adding_score_for_user + dice_user
                            if check_user > win_score:
                                adding_score_for_user += 1
                                print("Ace convert into 1")
                                print(f"Your score is: {adding_score_for_user}")
                                user.append(1)
                        else:
                            adding_score_for_user += dice_user
                            print(f"Your score is: {adding_score_for_user}")
                            user.append(dice_user)
                            if adding_score_for_user >= win_score:
                                loop_run = False
                                loop = False
                                running = False
                    else:
                        option_for_computer = random.choice(cards)
                        if option_for_computer == 11:
                            check_computer = adding_score_for_computer + option_for_computer
                            if check_computer > win_score:
                                adding_score_for_computer += 1
                                computer.append(1)
                        else:
                            adding_score_for_computer += option_for_computer
                            computer.append(option_for_computer)
                            if adding_score_for_computer >= win_score:
                                loop_run = False
                                loop = False
                                running = False
    print(f"User list: {user} , Computer list: {computer}")
    print(f"User score is: {adding_score_for_user} , Computer score is: {adding_score_for_computer}")
    if adding_score_for_computer > adding_score_for_user:
        print(f"User win...")
    elif adding_score_for_user > adding_score_for_computer:
        print(f"Computer win...")
    if input("---Do you want to play again 'y' for play and 'n' for quit the game ..? ").lower() == 'y':
        start()


start()
