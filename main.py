from psychopy import visual, core, event  # import some libraries from PsychoPy
from random import choices
from set_utils import cards

path =  '/Users/labc02/Documents/GitHub/Set_Recognition/pics/'

 #create a window
win = visual.Window([800,600], monitor="testMonitor", units="deg")

for round in range(5):
    hand = choices(cards.deck_1, k = 3) # deal cards from deck
    #create visual objects to present
    msg_1 = visual.TextStim(win, text = 'Is this a Set?', pos = (0, 5))
    card_1 = visual.ImageStim(win, image = path+hand[0].picture, size = 5, pos = (-7, 0))
    card_2 = visual.ImageStim(win, image = path+hand[1].picture, size = 5, pos = (0, 0))
    card_3 = visual.ImageStim(win, image = path+hand[2].picture, size = 5, pos = (7, 0))
    msg_2 = visual.TextStim(win, text = 'Tap on the spacebar if this is a Set.', pos = (0, -5), height= 0.7)
    
    #draw the stimuli and update the window
    msg_1.draw()
    card_1.draw()
    card_2.draw()
    card_3.draw()
    msg_2.draw()
    win.update()

    trial_clock = core.Clock() # start the clock
    responses = event.waitKeys(10, timeStamped = trial_clock) # wait for the response and record it
    print(responses)