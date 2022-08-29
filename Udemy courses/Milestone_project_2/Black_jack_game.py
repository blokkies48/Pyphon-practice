import random

#Dict of the different values to be used for reverance to the ranks
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
#List of posible suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
#List of all posible ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]


    def __str__(self):
            return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()

class HumanPlayer:
    def __init__(self, money):
        self.money = money
        self.player_hand = []

    def add_card(self, card):
        return self.player_hand.append(card)


    def place_bet(self, bet_amt):
        return bet_amt

class Dealer:
    def __init__(self):
        self.dealer_hand = []

    def add_card(self, card):
        return self.dealer_hand.append(card)


deck = Deck()
player = HumanPlayer(100)
deck.shuffle()
dealer_main = Dealer()
pot_prize = 0


game_on = True

while game_on:
    player_bet = 0
    player_hand_value = []
    player_cards = []
    dealer_hand_value = []
    sum_dealer_hand = 0



    
    want_to_place_bet = input("Do you want to place a bet Y/N").upper()
    if want_to_place_bet == "Y":
        while True:
            player_bet = player.place_bet(int(input("Place a bet ")))
            if player_bet <= player.money:
                player.money = player.money - player_bet
                print(f"---Your bet is {player_bet}")
                print(player.money)
                break
            else:
                print("not enough money")
    else:
        print("---Player passes")

    if len(player.player_hand) ==  0:
        (player.add_card(deck.deal_card()))
        (player.add_card(deck.deal_card()))
    else:
        while True:
            hit = input("Press 'h' to hit, 's' to stand").upper()
            if hit == "H":
                (player.add_card(deck.deal_card()))
                print("---Hit" )
                break
            elif hit == "S":
                print("---Stand")
                break

    for card in player.player_hand:
        player_hand_value.append(card.value) 
        player_cards.append(card)
    print("---Your cards are")
    for card in player_cards:
        print(card)
    
    print("---Value of your cards are")
    print(sum(player_hand_value))
    
    for card in dealer_main.dealer_hand:
        dealer_hand_value.append(card.value)
    sum_dealer_hand = sum(dealer_hand_value)

    if len(dealer_main.dealer_hand) == 0:
        dealer_main.add_card(deck.deal_card())
        dealer_main.add_card(deck.deal_card())
      
        
    else:
        if sum_dealer_hand <= 17:
            dealer_main.add_card(deck.deal_card())
            print("Took on card")
         
        else:
            print("---Dealer passed")
           
    print("---Dealer hand value")
    print(sum(dealer_hand_value))
    

    #Win checks
    player_win = False
    pot_prize += (player_bet * 2)
    print("pot prize")
    print(pot_prize)

    if player_win == True:
        player.money += pot_prize