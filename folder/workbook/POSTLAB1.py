class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs(node, target_value, depth):
    if node.value == target_value:
        return True
    if depth <= 0:
        return False
    for child in node.children:
        if dfs(child, target_value, depth - 1):
            return True
    return False

def ids(root, target_value):
    depth = 0
    while True:
        if dfs(root, target_value, depth):
            return depth
        depth += 1

# Example tree
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3), TreeNode(4)]
root.children[0].children = [TreeNode(5), TreeNode(6)]
root.children[2].children = [TreeNode(7), TreeNode(8), TreeNode(9)]

target_value = 8
depth = ids(root, target_value)

if depth != None:
    print("Target value found at depth:", depth)
else:
    print("Target value not found")
