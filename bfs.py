def solve(maze):
    visited = set([maze.start])  # keep track of visited cells via hashset
    paths = [[maze.start]]  # record all paths as we build them
    grid = maze.grid
    direction = ((0, 1), (-1, 0), (1, 0), (0, -1))
    while paths:
        # we will extend each path in paths by one cell and store them in new_paths
        # then we will set paths = new_paths and repeat
        new_paths = []
        for path in paths:
            pos = path[-1]  # the current cell we are at in the maze
            r = pos[0]  # row
            c = pos[1]  # column
            for dr, dc in direction:  # try all four directions
                if 0 <= r+dr < maze.m and 0 <= c+dc < maze.n and (r+dr, c+dc) not in visited and grid[r+dr][c+dc] == 1:
                    # the cell extension is within the bounds of the maze and is unvisited pathway cell
                    # add it to the current path
                    spot = (r+dr, c+dc)
                    visited.add(spot)
                    new_path = path[:]
                    new_path.append(spot)
                    new_paths.append(new_path)
                    if spot == maze.end:  # we are at the exit cell of the maze
                        return new_paths[-1]  # return the path that got us there
        paths = new_paths
    return []  # no solution, return empty set since there are no valid paths from entrance to exit
