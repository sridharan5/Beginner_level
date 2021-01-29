import art
import game_data
import random
print(art.logo)
name = []
followers = []
description = []
country = []
for i in game_data.data:
    name.append(i['name'])
    followers.append(i['follower_count'])
    description.append(i['description'])
    country.append(i['country'])
val = random.randint(0, followers.__len__()-1)
print_name = name[val]
print_description = description[val]
print_country = country[val]
a = followers[val]
score = 0
for i in range(1, followers.__len__()):
    print(f"Current_score is : {score}")
    print(f"Compare A: {print_name}, {print_description}, {print_country} .")
    ran = random.randint(1, followers.__len__()-1)
    b = followers[ran]
    print_name = name[ran]
    print_description = description[ran]
    print_country = country[ran]
    print(art.vs)
    print(f"Compare B: {print_name}, {print_description}, {print_country} .")
    option = input("Type 'h' for 'Higher' and 'l' for Lower: ").lower()
    if option == 'h':
        if a <= b and a != b:
            score += 1
            a = b
        else:
            break
    if option == 'l':
        if a >= b and a != b:
            score += 1
            a = b
        else:
            break
    else:
        print("Please check you input whether it is 'h' or 'l' ....")
if score != 0 and score != followers.__len__()-1:
    print(f"Almost reached keep trying. Your score is {score} .")
elif score == followers.__len__()-1:
    print(f"Great you smashed the game man! your record is: {score}")
else:
    print(f"You loose! you got {score} score .")