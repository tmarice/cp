
node *insert(node *root, int value) {
  if (root == NULL) {
    node *n = new node();
    n->data = value;
    return n;
  }

  if (value < root->data) 
    root->left = insert(root->left, value);
  else
    root->right = insert(root->right, value);

  return root;
}

