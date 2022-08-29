from random import randint

def blackjack(args):
    if sum(args) <= 21:
        return sum(args)
    elif sum(args)> 21 and 11 in args:
        if sum(args) - 10 > 21:
            return sum(args)
        return sum(args) -10
    elif sum(args)> 21:
        return sum(args)


def player_hand():
    card_amount = 0
    hand_total = []
    player_input = input("Type 'h' to hit or anything else to stop ")

    while player_input.upper() == 'H':
        card_amount = randint(1,11)
        hand_total.append(card_amount)
        print(hand_total)
        player_input = input("Type hit to hit or anything else to stop ")

    return hand_total

def dealer():
    dealer_hand = 0
    while dealer_hand < 17:
        dealer_hand += randint(1,10)
    return dealer_hand

def win_con(player_hand, dealer_hand):
    if dealer_hand > 21 and player_hand <= 21:
        return f"----Dealer bust!! Dealer hand = {dealer_hand}, Yours ={player_hand}"
    elif player_hand > 21 and dealer_hand <= 21:
        return f"----Bust!! Dealer hand = {dealer_hand}, Yours ={player_hand}"
    elif player_hand > 21 and dealer_hand > 21:
        return f"----Bust Both!! Dealer hand = {dealer_hand}, Yours ={player_hand}"
    elif dealer_hand == player_hand:
        return f"----Draw!! Dealer hand = {dealer_hand}, Yours ={player_hand}"
    elif dealer_hand > player_hand:
        return f"----Dealer wins!! Dealer hand = {dealer_hand}, Yours ={player_hand}"
    elif dealer_hand < player_hand:
        return f"----You win!! Dealer hand = {dealer_hand}, Yours ={player_hand}"
    elif dealer_hand == 21:
        return f"----Dealer wins!! Dealer hand = {dealer_hand}, Yours ={player_hand}"
    elif player_hand == 21:
        return f"----You win!! Dealer hand = {dealer_hand}, Yours ={player_hand}"

play_game = input("Do you want to play y/n? ")

while play_game.upper() == 'Y':
    
        print(win_con(blackjack(player_hand()),dealer()))
        play_game = input("Do you want to play y/n? ")

