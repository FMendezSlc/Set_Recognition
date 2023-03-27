class Card:
    
    def __init__(self, shape, filling, color, number, picture):
        self.shape = shape
        self.filling = filling
        self.color = color
        self.number = number
        self.picture = picture

ofbd = Card(shape = 'diamond', filling = 'solid', color = 'black', number = 'one', picture = 'ofbd.png')
ofbo = Card(shape = 'oval', filling = 'solid', color = 'black', number = 'one', picture = 'ofbo.png')
ofbr = Card(shape = 'rectangle', filling = 'solid', color = 'black', number = 'one', picture = 'ofbr.png')

deck_1 = [ofbd, ofbo, ofbr]