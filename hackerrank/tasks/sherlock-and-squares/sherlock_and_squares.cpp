#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
  int t;

  cin >> t;

  while (t--) {
    int a, b;
    cin >> a >> b;

    int lo = int(ceil(sqrt(a)));
    int hi = int(floor(sqrt(b)));

    cout << max(hi - lo + 1, 0) << endl;
  }

  return 0;
}
