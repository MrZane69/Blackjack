import random
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 
          'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='ace':
            self.aces+=1
    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1
def show_some(player,dealer):
    print("\ndealershand:", *dealer.cards,sep='\n ')
    print("dealershand=", dealer.value)
    print("\nplayershand:", *player.cards,sep='\n ')
    print("playershand=", player.value)
def show_all(player,dealer):
    print("\ndealershand:", *dealer.cards,sep='\n ')
    print("dealershand=", dealer.value)
    print("\nplayershand:", *player.cards,sep='\n ')
    print("playershand=", player.value)
def hs(deck, hand):
    global playing
    while True:
        choice = input("hit me 'h' or stay 's'")
        if choice.lower()=='h':
            hand.add_card(deck.deal())
            hand.adjust_for_ace()
        elif choice.lower()=='s':
            print("chicken")
            playing = False
        else:
            print("stupid nincompoop")
            continue
        break
def bussin(player,dealer):
    print("player busts you suck at this game go do something better you stupid ignorant pos go buy scratchers or sum you cannot gamble for crap if you dont tell me to stop ill keep going, you are wasting your money sheldon")
def thedub(player,dealer):
    print("you did it sheldon")
def dbuss(player,dealer):
    print("man they need a new dealer")
def ddub(player,dealer):
    print("skibidi dealer won you need to be flushed")
def push(player,dealer):
    print("tie fight the dealer to the death shelon use pot of greed on him and draw 2 additional cards from your deck, then play another pot of greed, then play another")
def play_blackjack(credits):
    global playing
    print("heyhey welcome to the blackjack table sheldon, yes i know your name your the best theoretical physician of all time, the G.O.A.T of all time")
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    show_some(player_hand, dealer_hand)
    playing=True
    while playing:
        hs(deck,player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            bussin(player_hand, dealer_hand)
            credits -= 10
            break
    if player_hand.value <= 21:
        while dealer_hand.value <17:
            dealer_hand.add_card(deck.deal())
        show_all(player_hand, dealer_hand)
        if dealer_hand.value >21:
            dbuss(player_hand, dealer_hand)
            credits +=10
        elif dealer_hand.value > player_hand.value:
            ddub(player_hand, dealer_hand)
            credits -=10
        elif dealer_hand.value < player_hand.value:
            thedub(player_hand, dealer_hand)
            credits +=10
        else:
            push(player_hand, dealer_hand)
    return credits
