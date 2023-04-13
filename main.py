from psychopy import visual, core, event, data, gui  # import some libraries from PsychoPy
from random import choice
from set_utils import cards, functions # my own files

path =  '/Users/labc02/Documents/GitHub/Set_Recognition/pics/'

exp_info = {'subjectID':'test_sub',
            'age':23, 
            'date': data.getDateStr(),
            'experiment_type': 'Standard'}

filename = f"{exp_info['subjectID']}_{exp_info['date']}"

current_exp = data.ExperimentHandler(
        name='Set_Recognition', version='h.0.1', #not needed, just handy
        extraInfo = exp_info, #the info we created earlier
        dataFileName = filename, # using our string with data/name_date
        )

#create a window
win = visual.Window([800,600], monitor="testMonitor", units="deg")

dlg = gui.DlgFromDict(exp_info, title='Rgistration', fixed=['experiment_type', 'date'])

# welcome and instructions
functions.welcome(win)
#instructions
functions.instructions(win)
#Examples
functions.examples(win, path)

conditions = {'nTrails': 5, 'iti': 0.0, 'holding': 10, 'timeOut': 5}
block = 0

for deck in cards.decks:

    hands = functions.prepare_rounds(deck, propSets= 0.5, rounds= conditions['nTrails'])
    block += 1
    trialHandler = data.TrialHandler(trialList = [], nReps= conditions['nTrails'], dataTypes= ['block', 'correctResp', 'setLevel', 'userResp', 'RT'], extraInfo=exp_info) # object to control trial config and data storage

    current_exp.addLoop(trialHandler)

    for trial in trialHandler:
        
        trialHandler.addData('block', block) # log block number (block refers to the number of dimensions)
        hand = choice(hands)
        real_answer = functions.is_a_set(hand) # evaluate the hand, is it a set?
        trialHandler.addData('correctResp', real_answer)

        if real_answer:
            level = functions.set_level(hand) # determine the level of the set if it's a set
            print(level)
            trialHandler.addData('setLevel', level)

        #create visual objects to present
        msg_1 = visual.TextStim(win, text = 'Is this a Set?', pos = (0, 5))
        card_1 = visual.ImageStim(win, image = path+hand[0].picture, size = 5, pos = (-7, 0))
        card_2 = visual.ImageStim(win, image = path+hand[1].picture, size = 5, pos = (0, 0))
        card_3 = visual.ImageStim(win, image = path+hand[2].picture, size = 5, pos = (7, 0))
        msg_2 = visual.TextStim(win, text = 'Tap on the spacebar if this is a Set.\nPress Shift if it\'s not.', pos = (0, -5), height= 0.7)

        # --> inter-trial interval goes here if necessary <--

        #draw the stimuli and update the window
        msg_1.draw()
        card_1.draw()
        card_2.draw()
        card_3.draw()
        msg_2.draw()
        win.flip()

        response_clock = core.Clock() # start the clock

        # --> holding time can be modified here <--
        responses = event.waitKeys(10, timeStamped = response_clock, keyList = ['space', 'rshift', 'lshift']) # wait for the response and record it
        if responses == None:
            trialHandler.addData('userResp', 'Missed')
            msg_missed = visual.TextStim(win, text = 'You missed the trial!!', pos = (0, 0), height = 1.5)
            msg_missed.draw()
            win.flip()
            core.wait(0.3)
        else:
            if responses[0][0] == 'space' :
                user_answer = True
            else:
                user_answer = False

            trialHandler.addData('userResp', user_answer)
            trialHandler.addData('RT', responses[0][1])

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

        current_exp.nextEntry()

current_exp.close()