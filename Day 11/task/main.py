import art
import random
print(art.logo)

#Creates a dictionary of cards and their values
cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

#Step 1 ask user if they would like to play a game of blackjack
def start_game():
    play_again = ''
    while play_again != 'y' and play_again != 'n':
        play_again = input("Would you like to play a hand? y or n: ").lower()
        if play_again == 'y':
            play_blackjack()
        if play_again == 'n':
            print("Thank you for playing!")
            exit()
#Step 2 ask for a bet and keep it with a running total

#Step 3 check total money and then ask for a bet

#Step 4 Deal cards to player and computer, display 2nd computer card. Calculate 21 auto wins.
def play_blackjack():
    player_total = 0
    computer_total = 0
    drawn_cards=[]
    #Deals 4 cards randomly and assigns them to a list.
    for i in range(4):
        random_card = random.choice(list(cards.keys()))
        drawn_cards.append(random_card)
    print(drawn_cards)
    print(f"Computer Cards:\n {art.unknown_card} {art.card_art[drawn_cards[1]]}")
    print(f"Player Cards: \n {art.card_art[drawn_cards[2]]} {art.card_art[drawn_cards[3]]}")


    computer_total = int(cards[drawn_cards[0]]) + int(cards[drawn_cards[1]])
    player_total = int(cards[drawn_cards[2]]) + int(cards[drawn_cards[3]])

    #Checks for an auto win / loss / tie scenario with blackjacks.

    if  computer_total == 21:
        if  player_total == 21:
            print("Wow! You both have blackjacks. Tie")
        else:
            print("Computer wins with a blackjack.")
        start_game()
    elif player_total == 21:
            print("You have a blackjack! You win")
    print(cards[drawn_cards[2]]+int(cards[drawn_cards[3]]))

    #Asks the player if they want to hit or stand. Then the player auto hits until it is over 17.
    hit_or_stand =''
    while hit_or_stand != 's' and hit_or_stand != 'PLAYER LOST':
        hit_or_stand=input("Hit (h) or stand (s): ")
        if hit_or_stand == 'h':
            random_card = random.choice(list(cards.keys()))
            print(art.card_art[random_card])
            player_total += cards[random_card]

            #Checks to see if an ace was drawn.
            if player_total == 21:
                hit_or_stand = 's'
            elif player_total > 21:
                if cards[random_card] == 11:
                    player_total -=10
                else:
                    print(f"Unfortunately {player_total} busts. You lose.")
                    hit_or_stand = 'PLAYER LOST'
            print(f"Your new total is {player_total}")

        elif hit_or_stand == 's':

            #Goes to a function that calculates the computer hitting until it hits over 17.
            computer_total = computer_hit_or_stand(computer_total, drawn_cards)
            if player_total > computer_total:
                print(f"Player has {player_total} which beats the computer that has {computer_total} :)")
            elif player_total < computer_total:
                print(f"Player has {player_total} which loses to the computer that has {computer_total} :(")
            else:
                print(f"The player and computer have tied with a score of {computer_total}.")
    start_game()
#Step 5: print total and cards. Ask whether they want to hit or stand. Comp auto hits under 17.
#Loop until player either busts or stands

#Step 6: Print totals of both the player and the machine, determine winner and then assign bets.
def computer_hit_or_stand(computer_total, drawn_cards):
    while computer_total < 17:
        random_card = random.choice(list(cards.keys()))
        print(art.card_art[random_card])
        if computer_total > 21:
            if cards[drawn_cards[0]] == 11:
                cards[drawn_cards[0]] = 1
            elif cards[drawn_cards[1]] == 11:
                cards[drawn_cards[1]] = 1
            elif cards[random_card] == 11:
                random_card = "1"
            else:
                print(f"Computer has {computer_total} which busts. You win!")
                start_game()
        computer_total += cards[random_card]
    return computer_total
start_game()