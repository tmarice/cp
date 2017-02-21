
def inOrder(root):
  if root is None:
    return

  inOrder(root.left)
  print root.data
  inOrder(root.right)
