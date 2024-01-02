from collections import deque
class Node: 
    def __init__(self, value):
        self.value = value;
        self.left = None;
        self.right = None;


def DFS(node):
    if node is None:
        return;
    print(node.value, end=" ");
    DFS(node.left);
    DFS(node.right);


def BFS(root):
    if root is None:
        return;
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ");
         # enqueue left child
        if node.left:
            queue.append(node.left)
        # enqueue right child
        if node.right:
            queue.append(node.right);


root = Node(1);
root.left =Node(2)
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
DFS(root);
BFS(root)
