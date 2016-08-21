#include <iostream>

using namespace std;


void print(int fives, int threes) {
  if (fives == 0 && threes == 0)
    cout << -1;
  else {
    for (int i = 0; i < fives; ++i)
      cout << "5";
    for (int i = 0; i < threes; ++i)
      cout << "3";
  }

  cout << endl;
}


int main() {
  int t;

  cin >> t;

  while (t--) {
    int n;
    cin >> n;

    int fives = 0, threes = 0;

    for (int i = n; i >= 0; --i)
      if (i % 3 == 0 && (n - i) % 5 == 0) {
        fives = i;
        threes = n - i;
        break;
      }

    print(fives, threes);
  }

  return 0;
}
