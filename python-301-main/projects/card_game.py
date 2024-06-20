class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["None", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):  # verander cmp later naar "value"
        # check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # suits are the same ... check ranks
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        # ranks are the same ...it's a tie
        return 0
    



    

kaart = Card(2, 4)
print(kaart)