import art
import game_data
import random

#Step 1 pick two accounts at random. If the same account is picked, re-pick the contestants.
#Step 2: Display both accounts and ask which one has more followers.
def pick_accounts():
    print(art.logo)
    account1 = 0
    account2 = 0
    while account1 == account2:
        account1 = random.randint(0,len(game_data.data)-1)
        account2 = random.randint(0,len(game_data.data)-1)
    print("Who has more followers?")
    print(f"{game_data.data[account1]['name']}, who is a / an {game_data.data[account1]['description'].lower()} from {game_data.data[account1]['country']}")
    print(art.vs)
    print(f"{game_data.data[account2]['name']}, who is a / an {game_data.data[account2]['description'].lower()} from {game_data.data[account2]['country']}")
    guess = ''
    while guess != "a" and guess != "b":
        guess = input("Who has more followers? a or b: ").lower()
    check_answer(account1, account2, guess)

#Step 3: Determine if the player is right and print the result along with the total number of followers
def check_answer(contestant1, contestant2,player_guess):
    right_answer =''
    higher_account= None
    lower_account= None
    if game_data.data[contestant1]['follower_count'] > game_data.data[contestant2]['follower_count']:
        right_answer = 'a'
        higher_account= contestant1
        lower_account= contestant2
    elif game_data.data[contestant1]['follower_count'] < game_data.data[contestant2]['follower_count']:
        right_answer = 'b'
        higher_account= contestant2
        lower_account= contestant1
    if player_guess == right_answer:
        print(f"Congratulations, you won! {game_data.data[higher_account]['name']} has {game_data.data[higher_account]['follower_count']} million followers"
              f" while {game_data.data[lower_account]['name']} has {game_data.data[lower_account]['follower_count']} million followers")
    else:
        print(
            f"Sorry, you lose! {game_data.data[higher_account]['name']} has {game_data.data[higher_account]['follower_count']} million followers"
            f" while {game_data.data[lower_account]['name']} has {game_data.data[lower_account]['follower_count']} million followers")
    play_again()

#Step 4: Ask the player if they would like to play again.
def play_again():
    again=''
    while again != 'y' and again != 'n':
        again = input("Would you like to play again? (y/n): ").lower()
    if again == 'y':
        print('\n' * 20)
        pick_accounts()
    elif again == 'n':
        print("Thank you for playing!")

pick_accounts()