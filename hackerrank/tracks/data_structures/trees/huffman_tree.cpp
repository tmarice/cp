
void decode_huff(node *root, string s) {
  node *cur = root;

  for (char c: s) {
    if (c == '0')
      cur = cur->left;
    else
      cur = cur->right;

    if (cur->data) {
      cout << cur->data;
      cur = root;
    }
  }
}

  

