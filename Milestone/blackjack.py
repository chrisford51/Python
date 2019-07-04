### Blackjack
### Milestone Project by Chris Ford

import random

##Setting up cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

##Card Class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

##Deck Class
class Deck:
    def __init__(self):
        self.deck = [] #Start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) #Build card objects and add them to the list

    def __str__(self):
        deck_comp = '' #Start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() #Add each card onject's print string
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

##Testing Deck
# test_deck = Deck()
# print(test_deck)

##Hand Class
class Hand:
    def __init__(self):
        self.cards = []     #Starts with an empty list
        self.value = 0      #Starts with zero value
        self.aces = 0       #add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_aces(self):
        pass


##Testing Hand and Value
test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
test_player.value

for card in test_player.cards:
    print(card)
