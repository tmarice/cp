#include <iostream>
#include <vector>


using namespace std;


typedef long long ll;
const int INF = 1000000000;

vector<int> r; 
int c[10002] = {0};


int get_c(int i) {
  if (i == r.size() - 1) // base case
    return 0;

  if (i == 0) // base case
    return 0;

  if (c[i]) // memoized solution
    return c[i];

  if (r[i] > r[i - 1] && r[i] <= r[i + 1])
    return c[i] = get_c(i - 1) + 1;
  else if (r[i] > r[i + 1] && r[i] <= r[i - 1])
    return c[i] = get_c(i + 1) + 1;
  else if (r[i] <= r[i + 1] && r[i] <= r[i - 1])
    return c[i] = 1;
  else if (r[i] > r[i + 1] && r[i] > r[i - 1])
    return c[i] = max(get_c(i - 1), get_c(i + 1)) + 1;
}

int main() {
  int n;

  cin >> n;

  r.push_back(-1);

  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;

    r.push_back(x);
  }

  r.push_back(r[r.size() - 1]);

  get_c(1);

  int total = 0;
  for (int i = 1; i <= n; ++i)
    total += c[i];

  cout << total << endl;

  return 0;
}




