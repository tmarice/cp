
def check_binary_search_tree_(root):
    """ every node in left subtree has to be smaller than root,
        every node in right subtree has to be greater that root.
    """

    if root is None:
        return True
    else:
        return check_bst(root, -1, 10**4+1)


def check_bst(root, cur_min, cur_max):
    if root is None:
        return True

    output = cur_min < root.data < cur_max
    output &= check_bst(root.left, cur_min, root.data)
    output &= check_bst(root.right, root.data, cur_max)

    return output
