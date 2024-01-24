from avl_tree import AVLNode
from draw_tree import draw_tree

if __name__ == "__main__":
    root = AVLNode(30)

    keys = [20, 35, 7, 25, 2, 3, 28, 27, 10, 5, 15, 40, 12, 32]

    for key in keys:
        root = root.insert(root, key)
        print("Inserted: ", key)

    print("AVL tree: ")
    print(root)

    # task 1 - find the node with minimum key
    min_node = root.min_value_node(root)
    print("Min key for the graph is: ", min_node.key)

    # task 2 - find the node with maximum key
    max_node = root.max_value_node(root)
    print("Max key for the graph is: ", max_node.key)

    # task 3 - find the sum of all node keys
    sum = root.find_node_keys_sum(root)
    print("Sum of all node keys is equal to: ", sum)

    # Draw the AVL-tree
    draw_tree(root, "AVL-tree")
