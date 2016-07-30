#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;


int main() {
  int n;
  string data[100] = {""};

  cin >> n;

  for (int i = 0; i < n; ++i) {
    int x;
    string s;
    cin >> x >> s;

    if (i < n/2)
      s = '-';

    data[x].append(s + " ");
  }

  for (int i = 0; i < 100; ++i) {
    cout << data[i];
  }

  cout << endl;

  return 0;
}
