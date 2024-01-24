import uuid

class AVLNode:
    def __init__(self, key, color="skyblue"):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None
        self.color = color
        self.id = str(uuid.uuid4())

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y):
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def delete_node(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                troot = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def find_node_keys_sum(self, root, sum=0):
        total = 0
        if root:
            total += root.key

            return (
                total
                + self.find_node_keys_sum(root.right, total)
                + self.find_node_keys_sum(root.left, total)
            )
        else:
            return total


if __name__ == "__main__":
    root = AVLNode(10)
    keys = [2, 3, 5, 15, 1, 4]

    for key in keys:
        root = root.insert(root, key)
        print("Inserted: ", key)
        print("AVL tree: ")
        print(root)
        print("Total node keys sum: ", root.find_node_keys_sum(root))

    # Delete
    keys_to_delete = [2, 10]
    for key in keys_to_delete:
        root = root.delete_node(root, key)
        print("Delete: ", key)
        print("AVL tree: ")
        print(root)
        print("Total node keys sum: ", root.find_node_keys_sum(root))
