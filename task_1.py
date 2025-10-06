class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def find_min(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.key
if __name__ == "__main__":
    root = None
    values = [20, 8, 22, 4, 12, 10, 14]
    for v in values:
        root = insert(root, v)
    print("Найменше значення у дереві:", find_min(root))