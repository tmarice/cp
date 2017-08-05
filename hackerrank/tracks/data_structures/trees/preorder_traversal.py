
def preOrder(root):
    if root:
        print root.data,

    if root.left is not None:
        preOrder(root.left)

    if root.right is not None:
        preOrder(root.right)
