from heapq import heappush, heappop

def astar(maze, start, end):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    frontier = []
    heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        current = heappop(frontier)[1]

        if current == end:
            break

        for dx, dy in neighbors:
            next_node = current[0] + dx, current[1] + dy
            if next_node[0] < 0 or next_node[0] >= len(maze) or next_node[1] < 0 or next_node[1] >= len(maze[0]):
                continue
            if maze[next_node[0]][next_node[1]] == 1:
                continue
            new_cost = cost_so_far[current] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(end, next_node)
                heappush(frontier, (priority, next_node))
                came_from[next_node] = current

    path = []
    current = end
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (0, 0)
end = (7, 6)

path = astar(maze, start, end)
print(path)
