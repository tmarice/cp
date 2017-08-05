#include <iostream>
using namespace std;

int main() {
  int n, x, res = 0;

  cin >> n;

  while (n--) {
    cin >> x;
    res ^= x;
  }

  cout << res << endl;

  return 0;
}

