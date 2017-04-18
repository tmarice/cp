#include <iostream>
#include <string>
#include <sstream>
#include <queue>
using namespace std;

typedef long long ull;

int memo_counter;

class Node {
  public:
    ull v;
    int id;
    Node *l, *r;

    Node(ull v): v(v), l(NULL), r(NULL) {
      if (v != -1)
        this->id = memo_counter++;
    }
};

int n;

ull memo[1000001];


ull get_max_port(Node *root) {
  ull res_take = 0;
  ull res_leave = 0;

  if (root->l != NULL)
    res_leave += memo[root->l->id] ? memo[root->l->id] : get_max_port(root->l);
  if (root->r != NULL)
    res_leave += memo[root->r->id] ? memo[root->r->id] : get_max_port(root->r);

  if (root->l) {
    if (root->l->l != NULL)
      res_take += memo[root->l->l->id] ? memo[root->l->l->id] : get_max_port(root->l->l);
    if (root->l->r != NULL)
    res_take += memo[root->l->r->id] ? memo[root->l->r->id] : get_max_port(root->l->r);
  }
  if (root->r) {
    if (root->r->l != NULL)
      res_take += memo[root->r->l->id] ? memo[root->r->l->id] : get_max_port(root->r->l);
    if (root->r->r != NULL)
      res_take += memo[root->r->r->id] ? memo[root->r->r->id] : get_max_port(root->r->r);
  }

  return memo[root->id] = max(res_take + root->v, res_leave);

}

int main() {
  cin >> n;

  if (n == 0) {
    cout << 0 << endl;
    return 0;
  }

  string s;

  getline(cin, s);
  getline(cin, s);
  stringstream ss(s);

  ull x;

  ss >> x;

  queue<Node*> q;
  Node *root = new Node(x);

  q.push(root);

  int count = 0;
  Node *cur;
  while (!ss.eof()) {
    ss >> x;
    if (!ss) {
      ss.clear();
      ss.ignore(1, ' ');
      x = -1;
    }

    Node *node = new Node(x);

    if (count == 0) {
      cur = q.front();
      q.pop();
    }

    if (count == 0) {
      ++count;

      if (x != -1)
        cur->l = node;
    }
    else {
      count = 0;

      if (x != -1)
        cur->r = node;
    }

    if (x != -1)
      q.push(node);
  }

  cout << get_max_port(root) << endl;

  return 0;
}


