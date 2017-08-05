
void iter_left(node *root) {
  if (root == NULL)
    return;

  iter_left(root->left);
  cout << root->data << " ";
}

void iter_right(node *root) {
  if (root == NULL)
    return;

  cout << root->data << " ";
  iter_right(root->right);
}

void top_view(node *root) {
  if (root == NULL)
    return;

  iter_left(root->left);
  cout << root->data << " ";
  iter_right(root->right);
}
