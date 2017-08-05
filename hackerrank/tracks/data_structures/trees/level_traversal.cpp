#include <queue>

using namespace std;


void LevelOrder(node *root) {
  if (root == NULL)
    return;

  queue<node*> q;
  q.push(root);

  while (!q.empty()) {
    node *cur = q.front();
    q.pop();
    cout << cur->data << " ";

    if (cur->left)
      q.push(cur->left);

    if (cur->right)
      q.push(cur->right);
  }
}

