class Maze:
    def __init__(self, img):
        self.n, self.m = img.size
        self.grid, row = [], []  # grid is a 2-d list that stores the maze structure (1 = wall, 0 = path)
        for i, pixel in enumerate(list(img.getdata(3))):
            row.append(0 if pixel == 255 else 1)
            if (i+1) % self.m == 0:  # row is full, advance downwards
                self.grid.append(row)
                row = []
        f1 = f2 = False
        for row in range(self.n):
            if self.grid[row][0] == 1:
                self.start = (row, 0)
                f1 = True
            if self.grid[row][self.n-1] == 1:
                self.end = (row, self.n-1)
                f2 = True
            if f1 and f2:  # entrance and exit both located
                break
