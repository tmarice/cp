#include <iostream>
#include <string>
using namespace std;

int main() {
  int n;
  string b;

  cin >> n >> b;

  int out = 0;
  for (int i = 0; i < n - 2; ++i)
    if (b[i] == '0' && b[i + 1] == '1' && b[i + 2] == '0') {
      ++out;
      i += 2;
    }

  cout << out << endl;

  return 0;
}


