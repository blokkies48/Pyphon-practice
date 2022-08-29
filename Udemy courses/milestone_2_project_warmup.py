import random
#Dict of the different values to be used for reverance to the ranks
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
#List of posible suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
#List of all posible ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#Card class for creating a card object
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


class Player:
    def __init__(self,name):
        self.name = name
        self.player_hand = []

    def remove_one(self):
        return self.player_hand.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.player_hand.extend(new_cards)
        else:
            self.player_hand.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.player_hand)} cards."


#Creating two players
player_one = Player("One")
player_two = Player("Two")


#Creating an instance of the deck
new_deck = Deck()
#Shuffling the created deck
new_deck.shuffle()
#Give each player 26 cards
for x in range(int(len(new_deck.all_cards)/2)):
    player_one.add_cards(new_deck.deal_card())
    player_two.add_cards(new_deck.deal_card())

game_on = True

round_num = 0

while game_on:
    round_num += 1
    print(f"Currently on round {round_num}")

    if len(player_one.player_hand) == 0:
        print("Player two won")
        game_on = False
        break

    if len(player_two.player_hand) == 0:
        print("Player one won")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    card_max = 5
    while at_war:
        print(player_one_cards[-1])
        print(player_two_cards[-1])
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print("1")
            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            print("2")
            at_war = False
            
        else:
            print("WAR")
            
            if len(player_one.player_hand) < card_max:
                print("Player one doesn't have enough cards")
                print("Player two wins")
                game_on = False
                break

            if len(player_two.player_hand) < card_max:
                print("Player two doesn't have enough cards")
                print("Player one wins")
                game_on = False
                break

            else:
                for num in range(card_max):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())