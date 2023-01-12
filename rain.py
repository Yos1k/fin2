from tkinter import *
from time import *
from math import *
from random import *

myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background='alice blue')
s.pack()

rainX = []
rainY = []
rainSpeed = []
rainLength = []
rainColour = []
drawnRain = []
bigRainColour = []
drops = 200

for i in range(drops):
    rainX.append(randint(0, 800))
    rainY.append(randint(-600, 0))
    rainSpeed.append(randint(5, 7))
    rainLength.append((randint(10, 20)))
    rainColour.append(choice(['light blue', 'light sky blue']))
    bigRainColour.append(choice(['blue', 'sky blue']))

    drawnRain.append(0)


for f in range(1000):
    for i in range(drops):
        if i < 100:
            drawnRain[i] = s.create_line(rainX[i], rainY[i], rainX[i], rainY[i] + rainLength[i], fill=bigRainColour[i], width=2)
            rainY[i] += rainSpeed[i] + 5
        else:
            drawnRain[i] = s.create_line(rainX[i], rainY[i], rainX[i], rainY[i] + rainLength[i], fill=rainColour[i])
            rainY[i] += rainSpeed[i]
        if rainY[i] > 820:
            rainY[i] = -rainLength[i]

    s.update()
    sleep(0.03)
    for i in range(drops):
        s.delete(drawnRain[i])


myInterface.mainloop()
