#include <iostream>
#include <cmath>
using namespace std;

int main() {
  int t;

  cin >> t;

  while (t--) {
    string s;

    cin >> s;
    int l = s.size();

    string message = "Funny";

    for (int i = 0, j = l-1; i < l/2, j > l/2; ++i, --j)
      if (abs(s[i+1] - s[i]) != abs(s[j] - s[j-1])) {
        message = "Not Funny";
        break;
      }

    cout << message << endl;
  }

  return 0;
}
