from psychopy import visual, core  # import some libraries from PsychoPy
from random import choices

path =  '/Users/labc02/Documents/GitHub/Set_Recognition/pics/'

deck = ['ofbo.png', 'ofbr.png', 'ofbd.png']

 #create a window
win = visual.Window([800,600], monitor="testMonitor", units="deg")

for round in range(3):
    hand = choices(deck, k = 3)
    #create some stimuli
    msg = visual.TextStim(win, text = 'Is this a Set?', pos = (0, 5))
    card_1 = visual.ImageStim(win, image = path+hand[0], size = 5, pos = (-7, 0))
    card_2 = visual.ImageStim(win, image = path+hand[1], size = 5, pos = (0, 0))
    card_3 = visual.ImageStim(win, image = path+hand[2], size = 5, pos = (7, 0))
    
    #draw the stimuli and update the window
    msg.draw()
    card_1.draw()
    card_2.draw()
    card_3.draw()
    win.update()

#pause, so you get a chance to see it!
    core.wait(5.0)