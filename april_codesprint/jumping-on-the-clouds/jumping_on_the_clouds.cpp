#include <iostream>
#include <vector>
using namespace std;

const int INF = 1000000000;

int memo[101];
vector<int> cs;

int find_min(int c) {
  if (c < 0)
    return INF

  if (c == 0)
    return 0;

  if (memo[c])
    return memo[c];

  if (cs[c])
    return INF;

  return min(find_min(c-1), find_min(c-2)) + 1;
}




int main() {
  int n;

  cin >> n;

  int c;
  for (int i = 0; i < n; ++i) {
    cin >> c;
    cs.push_back(c);
  }

  int m = find_min(n-1);

  cout << m << endl;

  return 0;
}




