
def height(root):
    if root is None:
        return -1

    height_left = height(root.left)
    height_right = height(root.right)

    return 1 + max(height_left, height_right)

    
