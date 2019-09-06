# Maze Solver
## About
This solver will find and display the shortest entrance-to-exit path when provided with a maze image with black pixels denoting walls and white pixels denoting pathway. Pixels will hereafter be referred to as *cells*.

## Installation
``$ git clone https://github.com/cjporteo/maze-solver``
<br>
``$ pip3 install pillow`` (for image processing/display)

## Functionality
Included are 11 unsolved mazes. These were generated from https://keesiemeijer.github.io/maze-generator/. They range in complexity from *maze1.png* being 20 x 20 cells to *maze11.png* being 1600 x 1600 cells.

To solve a specific maze, for example *maze2.png*, we do:
``$ python3 main.py 2`` 
<br>
We will be presented with the following graphic and textual output:

<br>

![Unsolved](https://scontent-yyz1-1.xx.fbcdn.net/v/t1.15752-9/69257536_2298413867088480_894433514986930176_n.png?_nc_cat=104&_nc_oc=AQkZHIc42OQl1eJJmXgTM9X8mENWtLx22gMhASygLRxFczLom_W0azkce4adbCoSdzs&_nc_ht=scontent-yyz1-1.xx&oh=1238cdc8f846ae84aa18470f12835f8e&oe=5E0E194A)<br>
![enter image description here](https://scontent-yyz1-1.xx.fbcdn.net/v/t1.15752-9/68472252_2462414593795633_3420680132568809472_n.png?_nc_cat=111&_nc_oc=AQmFHjFsfa1Y6KmdlKGLkdGnbdCJZyMjxrnXHjAUfAO-YBprrxAG5lDj7WjXWKo1Pgo&_nc_ht=scontent-yyz1-1.xx&oh=1d7885c57c7b1d7a85e45174ee0e08c8&oe=5E0955A4)<br>
![Solved](https://scontent-yyz1-1.xx.fbcdn.net/v/t1.15752-9/69507639_2388532594549525_2880544336754245632_n.png?_nc_cat=110&_nc_oc=AQlfjt3OhjNjBlODYbZ5cjOSIqDT2Acs87UG3DGSnLtHdBpu1YYJfjSeRU8DNMyB2oo&_nc_ht=scontent-yyz1-1.xx&oh=2be7f6a311fa5cf6497ad21479a8c393&oe=5E04BFE9)<br>
## Notes:

 - For a maze to be considered valid by the solver, the entrance/exit cells must be located on the sides of the maze, opposing each other.
 - Currently, only BFS is employed as a solution method. Next steps for this project would be to incorporate more sophisticated maze solving algorithms. *Dijkstra* and *A** come to mind. However, the computational overhead required to initialize the maze as a graph structure may counteract optimization these algorithms would provide.

