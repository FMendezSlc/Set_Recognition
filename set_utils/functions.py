from random import sample, choices, shuffle
from psychopy import visual, core, event

def welcome(win):
    '''Display a welcome message.'''
    msg_0 = visual.TextStim(win, text = 'Welcome to the Set Recognition Task', pos = (0, 5))
    msg_instructions_0 = visual.TextStim(win, text = 'Each round, you will be presented with 3 cards and you must decide if they are a Set or not.', 
                                         pos = (0, 0), height = 0.9)
    msg_0.draw()
    msg_instructions_0.draw()
    win.flip()
    event.waitKeys(10)

def instructions(win):
    '''Display instructions'''
    msg_0 = visual.TextStim(win, text = 'Each card has a shape of an specific color and filling.', pos = (0, 5))
    msg_instructions_0 = visual.TextStim(win, text = 'A Set if defined by a single rule:\nEach feature (i.e. shape, color and filling) must be identical or completly different in all cards.', 
                                         pos = (0, 0), height = 0.9)
    msg_0.draw()
    msg_instructions_0.draw()
    win.flip()
    event.waitKeys(10)

def examples(win, path):
    '''Display some examples of sets and not set.'''
    #Example 1
    msg_0 = visual.TextStim(win, text = 'Example', pos = (0, 5))
    card_1 = visual.ImageStim(win, image = path+'ofbo.png', size = 5, pos = (-7, 0))
    card_2 = visual.ImageStim(win, image = path+'ofbr.png', size = 5, pos = (0, 0))
    card_3 = visual.ImageStim(win, image = path+'ofbd.png', size = 5, pos = (7, 0))
    msg_instructions_0 = visual.TextStim(win, text = 'This is a Set', pos = (0, -5), height = 0.8)
    msg_0.draw()
    card_1.draw()
    card_2.draw()
    card_3.draw()
    msg_instructions_0.draw()
    win.flip()
    event.waitKeys(10)
    #Example 2
    card_1 = visual.ImageStim(win, image = path+'osuo.png', size = 5, pos = (-7, 0))
    card_2 = visual.ImageStim(win, image = path+'ofbr.png', size = 5, pos = (0, 0))
    card_3 = visual.ImageStim(win, image = path+'oeyd.png', size = 5, pos = (7, 0))
    msg_instructions_0 = visual.TextStim(win, text = 'This is also a Set', pos = (0, -5), height = 0.8)
    msg_0.draw()
    card_1.draw()
    card_2.draw()
    card_3.draw()
    msg_instructions_0.draw()
    win.flip()
    event.waitKeys(10)
    #Example 3
    card_1 = visual.ImageStim(win, image = path+'ofbo.png', size = 5, pos = (-7, 0))
    card_2 = visual.ImageStim(win, image = path+'ofbr.png', size = 5, pos = (0, 0))
    card_3 = visual.ImageStim(win, image = path+'oeyd.png', size = 5, pos = (7, 0))
    msg_instructions_0 = visual.TextStim(win, text = 'This is Not a Set', pos = (0, -5), height = 0.8)
    msg_0.draw()
    card_1.draw()
    card_2.draw()
    card_3.draw()
    msg_instructions_0.draw()
    win.flip()
    core.wait(7)
    msg_0 = visual.TextStim(win, text = 'Ready??\n\n\nTap on the spacebar if this is a Set.\nPress Shift if it\'s not.', 
                            pos = (0, 0))
    msg_0.draw()
    win.flip()
    core.wait(3)

def is_a_set(hand):
    '''Evaluate the attributes of the cards in the given hand (i.e. shape, color, filling and number)
      and determine if they are a set.'''
    
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
    '''Determine the level of the set at hand. The level of a set is determined
      by the number of dimensions of disimilarity.'''

    level = 0

    if len(set([card.shape for card in hand])) == 3:
        level += 1
    if len(set([card.filling for card in hand])) == 3:
        level += 1
    if len(set([card.color for card in hand])) == 3:
        level += 1
    if len(set([card.number for card in hand])) == 3:
        level += 1

    return level

def prepare_rounds(deck, prop_sets = 0.5, rounds = 30):
    '''Define the hands to be dealt in the current block with a predifined proportion of sets present (propSets), defaults to 0.5.'''

    num_of_sets = round(rounds * prop_sets)
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
    shuffle(hands)
    return hands

