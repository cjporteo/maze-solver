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

![Unsolved](https://i.imgur.com/2GODu36.png)<br>
![Text Output](https://i.imgur.com/WWs64QH.png)<br>
![Solved](https://i.imgur.com/76mvjSZ.png)<br>

## Notes:

 - For a maze to be considered valid by the solver, the entrance/exit cells must be located on the sides of the maze, opposing each other.
 - Currently, only BFS is employed as a solution method. Next steps for this project would be to incorporate more sophisticated maze solving algorithms. *Dijkstra* and *A** come to mind. However, the computational overhead required to initialize the maze as a graph structure may counteract optimization these algorithms would provide.

