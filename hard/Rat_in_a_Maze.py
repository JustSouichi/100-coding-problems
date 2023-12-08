def rat_in_maze(maze):
    def is_safe(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

    def solve_maze_util(x, y, path):
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            path[x][y] = 1
            return True

        if is_safe(x, y):
            path[x][y] = 1
            if solve_maze_util(x + 1, y, path):
                return True
            if solve_maze_util(x, y + 1, path):
                return True
            path[x][y] = 0  # backtrack

        return False

    path = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    if not solve_maze_util(0, 0, path):
        return None
    return path
