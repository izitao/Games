from game_data import data
import random
from art import logo, vs
from replit import clear


def give_account():
    global game_data
    return game_data.pop(random.randint(0,len(game_data)-1))

def describe_accounts(account_1, account_2):
    print(f"Compare A: {account_1['name']}, a {account_1['description']}, from {account_1['country']}.")
    print(vs)
    print(f"Compare B: {account_2['name']}, a {account_2['description']}, from {account_2['country']}.")
    return str(input('Who has more followers? Type "A" or "B"')).upper()


game_data = data
game_active = True
score = 0
round = 1

while game_active == True:
    clear()
    print(f"ROUND {round}!")
    if round == 1: # FIRST ROUND
        account_1 = give_account()
        account_2 = give_account()
        print(logo)
        guess = describe_accounts(account_1, account_2)

        if guess.upper() == 'A' and account_1['follower_count'] > account_2['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
            round += 1
        elif guess.upper() == 'B' and account_1['follower_count'] < account_2['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
            round += 1
        else:
            print('End of the game')
            game_active = False
            print(f"Your final is: {score}.")

    if round > 1: # NEXT ROUNDS
        print(logo)
        print(f"You're right! Current score: {score}")
        account_1 = account_2
        account_2 = give_account()
        guess = describe_accounts(account_1, account_2)

        if guess.upper() == 'A' and account_1['follower_count'] > account_2['follower_count']:
            score += 1
            round += 1
        elif guess.upper() == 'B' and account_1['follower_count'] < account_2['follower_count']:
            score += 1
            #print("You're right")
            round += 1
        else:
            print('WRONG ANSWER! End of the game.')
            print(f"Your final score is: {score}.")
            game_active = False

    if len(game_data) == 0: #WINNING THE GAME
        print('You won the game!')
        print(f"Your final is: {score}.")
        game_active = False


