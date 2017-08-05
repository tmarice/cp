
int height(node *x) {
  if (x == NULL)
    return -1;
  else
    return x->ht;
}

int balance_factor(node *x) {
    return height(x->left) - height(x->right);
}

node *new_node(int val) {
    node *root = new node();
    root->left = NULL;
    root->right = NULL;
    root->val = val;
    root->ht = 0;

    return root;
}

node *rotate_left(node *z) {
  node *y = z->right;
  node *yl = y->left;

  y->left = z;
  z->right = yl;

  z->ht = max(height(z->left), height(z->right)) + 1;
  y->ht = max(height(y->left), height(y->right)) + 1;

  return y;
}

node *rotate_right(node *z) {
  node *y = z->left;
  node *yr = y->right;

  y->right = z;
  z->left = yr;

  z->ht = max(height(z->left), height(z->right)) + 1;
  y->ht = max(height(y->left), height(y->right)) + 1;

  return y;
}

node *insert(node *root, int val) {
  if (root == NULL) {
    return new_node(val);
  }

  if (val < root->val)
    root->left = insert(root->left, val);
  else 
    root->right = insert(root->right, val);

  root->ht = max(height(root->left), height(root->right)) + 1;
  int bf = balance_factor(root);

  if (bf > 1) {
    // left subtree unbalanced
    if (val < root->left->val) {
      // left left case
      return rotate_right(root);
    }
    else {
      // left right case
      root->left = rotate_left(root->left);
      return rotate_right(root);
    }
  }
  if (bf < -1) {
    // right subtree unbalanced
    if (val < root->right->val) {
      // right left case
      root->right = rotate_right(root->right);
      return rotate_left(root);
    }
    else {
      // right right case
      return rotate_left(root);
    }
  }

  return root;
}
