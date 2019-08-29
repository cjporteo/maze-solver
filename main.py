from PIL import Image  # for processing the .png images
import time  # tracking runtime
from maze import Maze  # our class for handling each maze
from mazedisplay import *  # displaying the unsolved and solved mazes
import bfs  # solving algorithm
from sys import argv

default = 1  # default maze difficulty level if no parameter is passed
level = int(argv[1]) if len(argv) > 1 else default

filename = "./maze-images/maze" + str(level) + ".png"

print("\n----ATTEMPTING MAZE LEVEL {}----------------------------------------------------------".format(level))

print("\nOPENING IMAGE")
t0 = time.time()

try:
    img = Image.open(filename)  # open the image
    print("IMAGE LOADED SUCCESSFULLY")
except FileNotFoundError:
    print("IMAGE FAILED TO LOAD")

disp(img, 1000)  # display the unsolved maze
res = img.copy() # a copy of the image - we will draw the solution path on top of this
t1 = time.time()
print("Time Elapsed: {0:.2f} ms\n".format(1000*(t1-t0)))

print("MAZE DIMENSIONS: {}x{}\n".format(img.size[0]-1, img.size[1]-1))

print("INITIALIZING MAZE")
maze = Maze(img)  # initialize the maze bject
t2 = time.time()
print("Time Elapsed: {0:.2f} ms\n".format(1000*(t2-t1)))

time.sleep(2)

print("COMMENCING BREADTH FIRST SEARCH...\n")
path = bfs.solve(maze)  # calls the solver
t3 = time.time()

if path:
    print("MAZE SOLVED")
    print("Time Elapsed: {0:.2f} ms\n".format(1000*(t3-t2-2)))
    drawpath(res, path, (255, 0, 0))  # draw the solution into the maze

    disp(res, 1000) # display the solved maze
    print("SHORTEST PATH LENGTH: {}".format(len(path)))
else:
    print("NO SOLUTION.\n")
    print("Time Elapsed: {0:.2f} ms".format(1000*(t3-t2-2)))
