# Imagine your company is building a series of card games and you are
# responsible for building the common API that the game developers will use.

# The game developers will want to be able to:
#  - Start each game with a new, full deck of cards
#  - Shuffle a deck: randomize the order of the cards
#  - Deal a card from a deck: return the first card of the deck and
#    remove that card from the deck so that it can't be dealt again

# The games will use a Standard 52-card deck which consists of:
#  - 4 suits:
#    Clubs, Diamonds, Hearts, Spades
#  - 13 ranks for each suit:
#    Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
# (See here for a visual:
# https://en.wikipedia.org/wiki/Standard_52-card_deck#Rank_and_color)

# Use any language you would like :)

from enum import Enum, auto
from random import randrange


class Card:

    @property
    def face(self):
        raise NotImplementedError

    @property
    def suit(self):
        raise NotImplementedError


class CardExtensions(Card):
    def __init__(self, face, suit):
        self._face = face
        self._suit = suit

    @property
    def face(self):
        return self._face

    @property
    def suit(self):
        return self._suit

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{{face: {}, suit {}}}".format(self._face, self._suit)


class FrenchCard(CardExtensions):

    class Suit(Enum):
        spades = auto()
        hearts = auto()
        clubs = auto()
        diamonds = auto()

    class Face(Enum):
        ace = 1
        two = 2
        three = 3
        four = 4

        five = 5
        six = 6
        seven = 7
        eight = 8
        nine = 9

        ten = 10
        jack = 11
        queen = 12
        king = 13

    def __str__(self):
        return "{{face: {}, suit {}}}".format(self._face.name, self._suit.name)


class Deck:
    def __init__(self, cardClass, numberOfDecks=1):
        if not issubclass(cardClass, Card):
            raise Exception
        self.cardClass = cardClass
        self.numberOfDecks = numberOfDecks
        self.numberOfCards = self.numberOfDecks * \
            len(self.cardClass.Suit) * len(self.cardClass.Face)

        self.cards = []
        for i in range(self.numberOfDecks):
            for s in cardClass.Suit:
                for f in cardClass.Face:
                    self.cards.append(cardClass(f, s))

        self.nextCardIdx = 0

    def shuffle(self, count=7):
        for n in range(count):
            for i in range(self.numberOfCards - 1):
                j = randrange(i + 1, self.numberOfCards)
                self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def deal(self):
        try:
            card = self.__next__()
        except StopIteration:
            card = None

        return card

    def __iter__(self):
        return self

    def __next__(self):
        if not self.nextCardIdx < self.numberOfCards:
            raise StopIteration

        card = self.cards[self.nextCardIdx]

        self.nextCardIdx += 1

        return card


###############################################################################

import unittest


class Test_DeckOfCards(unittest.TestCase):

    def test_1(self):
        aDeck = Deck(FrenchCard)
        # print(aDeck.cards)
        aDeck.shuffle()
        # print(aDeck.cards)
        # aCard = aDeck.deal()

        # for card in aDeck:
        #   print(card)

        print(aDeck.cards[0])
        print(aDeck.deal())
        print()
        print(aDeck.cards[1])
        print(aDeck.deal())
        print()
        print(aDeck.cards[2])
        print(next(aDeck))
        print()

        for card in aDeck:
            print(card)

        print(aDeck.deal())


if __name__ == '__main__':
    unittest.main()

