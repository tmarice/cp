#include <iostream>

using namespace std;

int main() {
  int n;
  int data[100] = {0};

  cin >> n;

  while (n--) {
    int x;
    cin >> x;

    data[x]++;
  }

  for (int i = 0; i < 100; ++i)
    for (int j = 0; j < data[i]; ++j)
      cout << i << " ";

  cout << endl;

  return 0;
}
