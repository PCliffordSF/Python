import random

class Card(object):

    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank

class DeckOfCards(Card):

    deck = []

    def __init__(self,Card):

        self.deck = []
        suit = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        rank = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

        for cardRank in rank:
            for cardSuit in suit:
                newCard = Card(rank = cardRank, suit = cardSuit)
                self.deck.append(newCard)


    def printDeck(self):
        for card in self.deck:
            print(card.rank, card.suit)
        print("printed deck of cards\n")


    def shuffleDeck(self):
        random.shuffle(self.deck)
        print("The cards have been shuffled\n")

    def shuffleAndDrawCards(self, numberOfCards = 5):
        self.shuffleDeck()
        for card in range(numberOfCards):
            drawnCard = self.deck.pop()
            print(drawnCard.rank,drawnCard.suit)
        print(numberOfCards, "Shuffled Cards\n")

