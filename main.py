from psychopy import visual, core, event  # import some libraries from PsychoPy
from random import choice
from set_utils import cards, functions

path =  '/Users/labc02/Documents/GitHub/Set_Recognition/pics/'

#create a window
win = visual.Window([800,600], monitor="testMonitor", units="deg")

# welcome and instructions
functions.welcome(win)
#instructions
functions.instructions(win)
#Examples
functions.examples(win, path)

for deck in cards.decks:

    rounds = 3
    hands = functions.prepare_rounds(deck, propSets= 0.5, rounds= rounds)

    for round in range(rounds):

        hand = choice(hands)
        real_answer = functions.is_a_set(hand)

        if real_answer:
            level = functions.set_level(hand)
        #create visual objects to present
        msg_1 = visual.TextStim(win, text = 'Is this a Set?', pos = (0, 5))
        card_1 = visual.ImageStim(win, image = path+hand[0].picture, size = 5, pos = (-7, 0))
        card_2 = visual.ImageStim(win, image = path+hand[1].picture, size = 5, pos = (0, 0))
        card_3 = visual.ImageStim(win, image = path+hand[2].picture, size = 5, pos = (7, 0))
        msg_2 = visual.TextStim(win, text = 'Tap on the spacebar if this is a Set.\nPress Shift if it\'s not.', pos = (0, -5), height= 0.7)

        #draw the stimuli and update the window
        msg_1.draw()
        card_1.draw()
        card_2.draw()
        card_3.draw()
        msg_2.draw()
        win.flip()

        trial_clock = core.Clock() # start the clock
        responses = event.waitKeys(10, timeStamped = trial_clock, keyList = ['space', 'rshift', 'lshift']) # wait for the response and record it
        if responses == None:
            msg_missed = visual.TextStim(win, text = 'You missed the trial!!', pos = (0, 0), height = 1.5)
            msg_missed.draw()
            win.flip()
            core.wait(0.3)
        else:
            if responses[0][0] == 'space' :
                user_answer = True
            else:
                user_answer = False

            if real_answer == user_answer:
                msg_correct = visual.TextStim(win, text = 'Correct!!', color = '#CCFF99', pos = (0, 0), height = 1.5)
                msg_correct.draw()
                win.flip()
                core.wait(0.3)
            else:  
                msg_wrong = visual.TextStim(win, text = 'Wrong!!\n:(', color = '#FF6666', pos = (0, 0), height = 1.5)
                msg_wrong.draw()
                win.flip()
                core.wait(0.4)
            print(user_answer)


