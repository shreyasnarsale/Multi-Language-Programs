# Binary Search Tree Operations in Python

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


class BST:
    def __init__(self):
        self.root = None

    # 1. INSERTION
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.data:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    # 2. SEARCH
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        elif key < root.data:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    # 3. DELETION
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self._delete(root.left, key)
        elif key > root.data:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # Node with two children: Find inorder successor
            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)

        return root

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    # 4. TREE TRAVERSALS
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# -------- MAIN PROGRAM --------
tree = BST()

# Insert nodes
elements = [50, 30, 70, 20, 40, 60, 80]
for el in elements:
    tree.insert(el)

print("BST Traversals:")
print("Inorder Traversal: ", end="")
tree.inorder(tree.root)

print("\nPreorder Traversal: ", end="")
tree.preorder(tree.root)

print("\nPostorder Traversal: ", end="")
tree.postorder(tree.root)

# Search Example
key = 40
print("\n\nSearching for", key, ":", "Found" if tree.search(key) else "Not Found")

# Delete Example
delete_key = 30
print("Deleting:", delete_key)
tree.delete(delete_key)

print("Inorder Traversal after Deletion: ", end="")
tree.inorder(tree.root)
print()
