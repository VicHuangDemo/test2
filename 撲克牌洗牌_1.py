import random

class Card():
    def __init__(self, value, suit):
        self.value=value
        self.suit=suit

    def __repr__(self):
        suits = {"h":"♡", "s":"♠", "d":"♢", "c":"♣"}
        values = {**{i:str(i) for i in range(2,10)}, 
        **{10:'T', 11:'J',12:'Q', 13:'K', 14:'A'}}
        return values[self.value] + suits[self.suit]

    
class StardardDeck():
    def __init__(self):
        self.cards = [Card(value, suit) for value in range(2,15) for suit in 'hsdc']
                
    def __repr__(self):
        return ' '.join([card.__repr__() for card in self.cards])

    def shuffule(self):
        random.shuffle(self.cards)
        
    def draw(self):
        return self.cards.pop(0)
    
if __name__=='__main__':
    deck = StardardDeck()
    print("標準撲克牌:", deck)
    deck.shuffule()
    print("把牌堆洗亂")
    randomCard = deck.draw()
    print("抽出最上方的牌:", randomCard)
    print("剩下的牌為:" ,deck)