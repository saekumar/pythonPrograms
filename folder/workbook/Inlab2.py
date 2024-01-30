# Function to find the minimum number of steps to reach the goal states
def min_steps_to_reach_goal():
    # Initial state (X=0, Y=0)
    x = 0
    y = 0

    # Set of visited states
    visited = set()
    # Queue for BFS
    queue = [(x, y, 0)]
    # Set of rules
    rules = [
        # Fill 4-gallon jug
        lambda x, y: (4, y),

        # Fill 5-gallon jug
        lambda x, y: (x, 5),

        # Empty 4-gallon jug
        lambda x, y: (0, y),
        # Empty 5-gallon jug
        lambda x, y: (x, 0),
        # Pour water from 4-gallon jug to 5-gallon jug
        lambda x, y: ((max(0, x - (5 - y))), (min(y + x, 5))),
        # Pour water from 5-gallon jug to 4-gallon jug
        lambda x, y: ((min(x + y, 4)), (max(0, y - (4 - x))))
    ]
    while queue:
        x, y, steps = queue.pop(0)

        # Check if current state is a goal state
        if x == 1:
            if y == 0 or y == 1 or y == 2 or y == 3 or y == 4:
                return steps

        # Apply each rule to generate new states
        for rule in rules:
            new_x, new_y = rule(x, y)

            # Check if new state is valid and not already visited
            if 0 <= new_x <= 4 and 0 <= new_y <= 5 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))
    return -1
print("Minimum number of steps to reach any of the goal states:", min_steps_to_reach_goal())
