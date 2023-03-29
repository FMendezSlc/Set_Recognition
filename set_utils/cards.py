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

oebd = Card(shape = 'diamond', filling = 'empty', color = 'black', number = 'one', picture = 'oebd.png')
oebo = Card(shape = 'oval', filling = 'empty', color = 'black', number = 'one', picture = 'oebo.png')
oebr = Card(shape = 'rectangle', filling = 'empty', color = 'black', number = 'one', picture = 'oebr.png')
osbd = Card(shape = 'diamond', filling = 'striped', color = 'black', number = 'one', picture = 'osbd.png')
osbo = Card(shape = 'oval', filling = 'striped', color = 'black', number = 'one', picture = 'osbo.png')
osbr = Card(shape = 'rectangle', filling = 'striped', color = 'black', number = 'one', picture = 'osbr.png')

deck_2 = deck_1 + [oebd, oebo, oebr, osbd, osbo, osbr]