#include <iostream>
#include <cmath>

using namespace std;


int main() {
  int n;

  cin >> n;

  int maj = 0, min = 0;
  int x;

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j) {
      cin >> x;

      if (i == j)
        maj += x;

      if (i + j == n - 1)
        min += x;
    }

  cout << abs(maj - min) << endl;

  return 0;
}


  


