class Card:
    
    def __init__(self, shape, filling, color, number, picture):
        self.shape = shape
        self.filling = filling
        self.color = color
        self.number = number
        self.picture = picture

#black cards, filled
ofbd = Card(shape = 'diamond', filling = 'solid', color = 'black', number = 'one', picture = 'ofbd.png')
ofbo = Card(shape = 'oval', filling = 'solid', color = 'black', number = 'one', picture = 'ofbo.png')
ofbr = Card(shape = 'rectangle', filling = 'solid', color = 'black', number = 'one', picture = 'ofbr.png')

deck_1 = [ofbd, ofbo, ofbr]

#black cards striped and empty
oebd = Card(shape = 'diamond', filling = 'empty', color = 'black', number = 'one', picture = 'oebd.png')
oebo = Card(shape = 'oval', filling = 'empty', color = 'black', number = 'one', picture = 'oebo.png')
oebr = Card(shape = 'rectangle', filling = 'empty', color = 'black', number = 'one', picture = 'oebr.png')
osbd = Card(shape = 'diamond', filling = 'striped', color = 'black', number = 'one', picture = 'osbd.png')
osbo = Card(shape = 'oval', filling = 'striped', color = 'black', number = 'one', picture = 'osbo.png')
osbr = Card(shape = 'rectangle', filling = 'striped', color = 'black', number = 'one', picture = 'osbr.png')

deck_2 = deck_1 + [oebd, oebo, oebr, osbd, osbo, osbr]

#yellow cards
ofyd = Card(shape = 'diamond', filling = 'solid', color = 'yellow', number = 'one', picture = 'ofyd.png')
ofyo = Card(shape = 'oval', filling = 'solid', color = 'yellow', number = 'one', picture = 'ofyo.png')
ofyr = Card(shape = 'rectangle', filling = 'solid', color = 'yellow', number = 'one', picture = 'ofyr.png')
oeyd = Card(shape = 'diamond', filling = 'empty', color = 'yellow', number = 'one', picture = 'oeyd.png')
oeyo = Card(shape = 'oval', filling = 'empty', color = 'yellow', number = 'one', picture = 'oeyo.png')
oeyr = Card(shape = 'rectangle', filling = 'empty', color = 'yellow', number = 'one', picture = 'oeyr.png')
osyd = Card(shape = 'diamond', filling = 'striped', color = 'yellow', number = 'one', picture = 'osyd.png')
osyo = Card(shape = 'oval', filling = 'striped', color = 'yellow', number = 'one', picture = 'osyo.png')
osyr = Card(shape = 'rectangle', filling = 'striped', color = 'yellow', number = 'one', picture = 'osyr.png')

#blue cards
ofud = Card(shape = 'diamond', filling = 'solid', color = 'blue', number = 'one', picture = 'ofud.png')
ofuo = Card(shape = 'oval', filling = 'solid', color = 'blue', number = 'one', picture = 'ofuo.png')
ofur = Card(shape = 'rectangle', filling = 'solid', color = 'blue', number = 'one', picture = 'ofur.png')
oeud = Card(shape = 'diamond', filling = 'empty', color = 'blue', number = 'one', picture = 'oeud.png')
oeuo = Card(shape = 'oval', filling = 'empty', color = 'blue', number = 'one', picture = 'oeuo.png')
oeur = Card(shape = 'rectangle', filling = 'empty', color = 'blue', number = 'one', picture = 'oeur.png')
osud = Card(shape = 'diamond', filling = 'striped', color = 'blue', number = 'one', picture = 'osud.png')
osuo = Card(shape = 'oval', filling = 'striped', color = 'blue', number = 'one', picture = 'osuo.png')
osur = Card(shape = 'rectangle', filling = 'striped', color = 'blue', number = 'one', picture = 'osur.png')

deck_3 = deck_2 + [ofyd, ofyo, ofyr, oeyd, oeyo, oeyr, osyd, osyo, osyr, ofud, ofuo, ofur, oeud, oeuo, oeur, osud, osuo, osur]

decks = [deck_1, deck_2, deck_3]