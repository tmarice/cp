#include <iostream>
#include <vector>
using namespace std;

int n, d;
vector<int> counts(20001, 0);
vector<int> bs;

int main() {
  cin >> n >> d;

  int x;
  for (int i = 0; i < n; ++i) {
    cin >> x;

    bs.push_back(x);
    counts[x] = i + 1;
  }

  int count = 0;
  for (int i = 0; i < n; ++i) {
    if (bs[i] + 2*d >= 20000)
      continue;

    int ai = counts[bs[i]];
    int aj = counts[bs[i] + d];
    int ak = counts[bs[i] + 2*d];

    if (ai && aj && ak && ai < aj && aj < ak)
      ++count;
  }


  cout << count << endl;

  return 0;
}




