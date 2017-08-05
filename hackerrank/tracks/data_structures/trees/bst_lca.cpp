
node *lca(node *root, int v1, int v2) {
  if (root == NULL)
    return NULL;

  if (root->data == v1 || root->data == v2)
    return root;

  node *left = lca(root->left, v1, v2);
  node *right = lca(root->right, v1, v2);

  if (left && right && left->data != right->data)
    return root;
  else if (left != NULL)
    return left;
  else
    return right;
}
