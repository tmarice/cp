
#include <iostream>
#include <string>
#include <cctype>
#include <cstring>
using namespace std;


int memo[1001][1001];

int solve(string &a, string &b, int i, int j) {
  //cout << i << " " << j << endl;
  if (i == -1 && j != -1)
    return 0;

  if (j == -1) {
    while (i > -1) {
      if (isupper(a[i])) {
        return 0;
      }
      --i;
    }
    return 1;
  }

  if (i >= 0 && j >= 0 && memo[i][j] != -1)
    return memo[i][j];

  int r;
  if (isupper(a[i])) {
    if (a[i] == b[j])
      r = solve(a, b, i-1, j-1);
    else
      r = 0;
  }
  else {
    if (a[i] == tolower(b[j]))
      r = solve(a, b, i-1, j-1) || solve(a, b, i-1, j);
    else
      r = solve(a, b, i-1, j);
  }

  return memo[i][j] = r;
}

int main() {
  int q;
  cin >> q;

  while (q--) {
    string a, b;
    memset(memo, -1, sizeof(memo));
    cin >> a >> b;

    cout << (solve(a, b, a.size() - 1, b.size() - 1) ? "YES" : "NO") << endl;
  }

  return 0;
}
