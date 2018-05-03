# ellipsesAnimation
Animating ellipses with coordinates taken from csv data.

## What is this exactly doing?

Reads coordinates from csv files with the following format:

| Time        | X coordinate          | Y coordinate |
| ------------- |:-------------:| -----:|

For example:

|          |             |    |
| ------------- |:-------------:| -----:|
| 0      | -25.527729 | -5.366551 |
| 0.04      | -25.452916      |   -5.3608 |
|  |      |     |

can be a sample entry of the csv file you are going to use.

---

There are also some extra options like saving each frame of the animation into a different png file. It is commented into the code but you can do whatever you want with it. 😄 

This script was meant to take a selected agent's (=ellipse) coordinates and animate it with a different color from the rest. You can remove this functionality by commenting the lines indicated inside the script.

I will be glad to hear any feedback or suggestion. Feel free to use it and save yourself some time.

