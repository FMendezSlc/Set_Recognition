from psychopy import visual, core  # import some libraries from PsychoPy
from pathlib import Path
 #create a window
win = visual.Window([800,600], monitor="testMonitor", units="deg")
 
path =  '/Users/labc02/Documents/GitHub/Set_Recognition/pics/'
#create some stimuli
card_1 = visual.ImageStim(win, image = path+'ofbo.png', size = 5, pos = (-7, 0))
card_2 = visual.ImageStim(win, image = path+'ofbr.png', size = 5, pos = (0, 0))
card_3 = visual.ImageStim(win, image = path+'ofbt.png', size = 5, pos = (7, 0))
 
#draw the stimuli and update the window
card_1.draw()
card_2.draw()
card_3.draw()
win.update()

#pause, so you get a chance to see it!
core.wait(5.0)