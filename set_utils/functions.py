from random import sample, choices

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

def prepare_rounds(deck, propSets = 0.5, rounds = 30):
    '''Define the hands to be dealt in the current block with a predifined proportion of sets present (propSets), defaults to 0.5.'''

    num_of_sets = round(rounds * propSets)
    set_count = 0
    not_sets = 0
    hands = []
    while len(hands) < rounds:
        if len(deck) == 3: # deal cards from deck_1
            hand = choices(deck, k = 3)

            if is_a_set(hand):
                if set_count < num_of_sets:
                    set_count +=1
                    hands.append(hand)

            else:
                if not_sets < (rounds-num_of_sets):
                    not_sets +=1
                    hands.append(hand)
        else:
            hand = sample(deck, k = 3)
            
            if is_a_set(hand):
                if set_count < num_of_sets:
                    set_count +=1
                    hands.append(hand)

            else:
                if not_sets < (rounds-num_of_sets):
                    not_sets +=1
                    hands.append(hand)
    return hands

