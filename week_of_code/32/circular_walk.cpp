
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;

typedef long long ll;

int rs[10000001];

void fill_rs(int n, int g, int seed, int p) {
  for (int i = 1; i < n; ++i)
    rs[i] = ((ll)rs[i-1] * (ll)g + (ll)seed) % p;
}

int get_rs(int x, int n) {
  return rs[(x + n) % n];
}

bool in_interval(int left, int right, int n, int t) {
  left = (left + n) % n;
  right %= n;

  if (left > right)
    return t >= left || t <= right;
  else
    return t >= left && t <= right;
}

int calc(int n, int s, int t) {
  stack<int> st;
  int left = s;
  int right = s;
  int i = 0;

  st.push(s);

  int new_left, new_right, cur;
  while (st.size() > 0) {
    cout << i << " " << left << " " << right << endl;
    if (in_interval(left, right, n, t))
      return i;

    new_left = left;
    new_right = right;
    while (st.size() > 0) {
      cur = st.top();
      st.pop();

      new_left = min(new_left, cur - get_rs(cur, n));
      new_left = min(new_left, cur + get_rs(cur, n) % n);
      new_right = max(new_right, cur + get_rs(cur, n));
      new_right = max(new_right, (cur + get_rs(cur, n) + n) % n);
    }

    int j = new_left;
    while (j != left)
      st.push(j++);

    j = new_right;
    while (j != right)
      st.push(j--);

    left = new_left;
    right = new_right;
    i += 1;
  }

  return -1;
}

int main() {
  int n, s, t, g, seed, p;

  cin >> n >> s >> t >> rs[0] >> g >> seed >> p;

  if (s == t)
    cout << 0 << endl;
  else {
    fill_rs(n, g, seed, p);

    cout << calc(n, s, t) << endl;
  }

  return 0;
}
