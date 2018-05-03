# Animating ellipses from csv files
# Ourania (Rania) Spantidi
# SIU Carbondale 2018

from matplotlib.animation import FuncAnimation
import os
import glob
import csv
import matplotlib.pyplot as plt
import copy
from matplotlib.patches import Ellipse
import matplotlib.animation as ani
import cv2

path = os.getcwd()
# If you have something more custom, like me, and you keep the data in a different path, just use it.

path = "C:\\Users\\Rania\\Desktop\\githubUpdate\\data"

# find all data files in given directory
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('*.{}'.format(extension))]
directory = os.listdir(path)
x = []
y = []
xList = []
yList = []
zList = []
global agent
fig = plt.figure(figsize=(4,4))

maxX = 0
xLimMinimum = 2000
xLimMaximum = -100
yLimMinimum = 2000
yLimMaximum = -100
maxT = 0
z = []
names = []

for files in directory:
    x = []
    y = []
    z = []
    firstEle = 0
    with open(files, 'r')as f:
        reader = csv.reader(f)
        time = 0
        # files : agent1, agent2 etc
        for row in reader:      # x = x coordinates for agent, y = y coordinates for agent
            z.append(row[0])
            x.append(row[1])
            y.append(row[2])
            if xLimMaximum < float(row[1]):
                xLimMaximum = float(row[1])
            if yLimMaximum < float(row[2]):
                yLimMaximum = float(row[2])
            if xLimMinimum > float(row[1]):
                xLimMinimum = float(row[1])
            if yLimMinimum > float(row[2]):
                yLimMinimum = float(row[2])
            if float(row[0]) > maxT and firstEle == 0:
                maxT = float(row[0])
                name = f.name
            firstEle += 1
        x = [float(i) for i in x]
        y = [float(i) for i in y]
        z = [float(i) for i in z]
        names.append(f.name)
        xList.append((copy.copy(x)))
        yList.append((copy.copy(y)))
        zList.append((copy.copy(z)))

frames = []
for j in range(0, len(zList)):
    f = []
    for i in range(0, len(zList[j])):
        f.append(round(zList[j][i] * 25))
    frames.append(copy.copy(f))

# for each agent i, frames[i][:] keeps the frames he is appearing in
print(xLimMaximum, xLimMinimum, yLimMaximum, yLimMinimum)
a = 0.8
ax = plt.axes(xlim=(xLimMinimum - a, xLimMaximum + a), ylim=(yLimMinimum - a, yLimMaximum + a))
print(abs(xLimMaximum) + abs(xLimMinimum))
print(abs(yLimMaximum) + abs(yLimMinimum))
fig.patch.set_visible(False)
ax.axis('off')
lst1 = []
lst2 = []
global N
ax.set_aspect('equal')
N = 0
for i in range(0, len(xList)):
    if frames[i][0] == 0:
        lst1.append(xList[i][0])
        lst2.append(yList[i][0])

maxFrames = -1
for item in frames:
    if item[len(item)-1] > maxFrames:
        maxFrames = item[len(item)-1]

# scat = ax.scatter(lst1, lst2)
global ellipses
ellipses = []


def update(i):
    final = []
    ells = []
    # New positions
    for k in range(0, len(xList)):
        lst = []
        if N in frames[k]:
            # in which position in frames was N found?
            position = frames[k].index(N)
            lst.append(xList[k][position])
            lst.append(yList[k][position])
        else:
            lst.append(-600)
            lst.append(-600)
        final.append((copy.copy(lst)))
        ells.append(Ellipse(xy=lst, width=0.7, height=0.1, angle=0, edgecolor='b', fill='y'))    # ells[i] is the ith ellipse
    # now I want to make each ellipse one patch.
    for item in range(0, len(ells)):
        manager(item, ells[item])
    increment()
    # If you want to save each frame, uncomment the next line
    # plt.savefig(str(N)+".jpg")
    return []


def manager(item, patch):
    xe, ye = patch.center
    ellipses[item].center = (xe, ye)
    return patch,


def increment():
    global N
    N += 1
# Construct the animation, using the update function as the animation director.

for k in range(0, len(xList)):
    lst = []
    if 0 in frames[k]:
        # in which position in frames was 0 found?
        position = frames[k].index(0)
        lst.append(xList[k][position])
        lst.append(yList[k][position])
    else:
        lst.append(-600)
        lst.append(-600)
    ell = Ellipse(xy=lst, width=0.7, height=0.1, angle=0, edgecolor='b', fill='y')

    ellipses.append(ell)
for e in ellipses:
    ax.add_patch(e)

# The following lines are basically animating with a different color one selected agent.
# You can comment them all and completely ignore them.

# select agent by using "agent_X.csv" from "names" list
index = names.index("agent_1.csv")
ellipses[index].set_facecolor('c')
ellipses[index].set_edgecolor('red')
# now what we want is find the number of frames the agent is active.
# so instead of beginning at 0, we should begin from whichever frame the agent we want starts
# also the new maxFrames should be the total number of frames the "lead agent" is active.
startingFrame = frames[index][0]
framesOfAgent = frames[index]
maxFrames = len(framesOfAgent)
N = startingFrame
print(N, maxFrames)

animation = FuncAnimation(fig, update, interval=25, repeat=False, frames=maxFrames)

ax.set_aspect('auto')
plt.show()
