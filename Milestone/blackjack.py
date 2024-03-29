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

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


    def show_some(player,dealer):
        print("\nDealer's Hand:")
        print(" <card hidden> ")
        print('',dealer.cards[1])
        print("\nPlayer's Hand:", *player.cards, sep='\n')

    def show_all(player,dealer):
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =",dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =",player.value)



##Testing Hand and Value
# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())
# test_player.value
#
# for card in test_player.cards:
#     print(card)

##Chips Class
class Chips:
    def __init__(self):
        self.total = 100 # Number of chips, can be set to any amount or supplied by user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(chips):

        while True:
            try:
                chips.bet = int(input('How many chips would you like to bet? '))
            except ValueError:
                print('Sorry, a bet must be an integer!')
            else:
                if chips.bet > chips.total:
                    print("Sorry, your bet can't exceed ",chips.total)
                else:
                    break

    def hit(deck,hand):
        hand.add_card(deack.deal())
        hand.adjust_for_ace()

    def hit_or_stand(deck,hand):
        global playng       #to control upcoming while loop

        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

            if x[0].lower() == 'h':
                hit(deck,hand)  #hit() function defined about

            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing. ")
                playing = False

            else:
                print("Sorry, please try again.")
                continue
            break
