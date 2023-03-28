def is_a_set(hand):
    '''Evaluate the attributes of the cards in the given hand (i.e. shape, color, filling and number) and determine if they are a set.'''
    
    if len(set([card.shape for card in hand])) == 2:
        return False
    elif len(set([card.filling for card in hand])) == 2:
        return False
    elif len(set([card.color for card in hand])) == 2:
        return False
    elif len(set([card.number for card in hand])) == 2:
        return False
    else:
        return True


def set_level(hand):
    '''Determine the level of the set at hand. The level of a set is determined by the number of dimensions of disimilarity.'''

    level = 0

    if len(set([card.shape for card in hand])) == 3:
        level += 1
    elif len(set([card.filling for card in hand])) == 3:
        level += 1
    elif len(set([card.color for card in hand])) == 3:
        level += 1
    elif len(set([card.number for card in hand])) == 3:
        level += 1
        
    return level