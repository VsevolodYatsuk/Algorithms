class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursively(self.root, key)

    def _insert_recursively(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self._insert_recursively(root.left, key)
        else:
            root.right = self._insert_recursively(root.right, key)
        return root

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursively(root.left, key)
        return self._search_recursively(root.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, root, result):
        if root:
            self._inorder_traversal_recursive(root.left, result)
            result.append(root.val)
            self._inorder_traversal_recursive(root.right, result)


if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("Последовательный обход BST (inorder traversal):")
    print(bst.inorder_traversal())

    search_key = 40
    if bst.search(search_key):
        print(f"Значение {search_key} найдено в BST.")
    else:
        print(f"Значение {search_key} не найдено в BST.")
