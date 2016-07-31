#include <iostream>
#include <string>

using namespace std;


int main() {
  int n;
  int c[30] = {0};
  
  cin >> n;

  for (int i = 0; i < n; ++i) {
    string s;
    cin >> s;

    int updates[30] = {0};
    for (int j = 0; j < s.size(); ++j)
      updates[s[j] - 'a'] = 1;

    for (int j = 0; j < 30; ++j)
      c[j] += updates[j];
  }

  int count = 0;
  for (int i = 0; i < 30; ++i)
    if (c[i] == n)
      ++count;

  cout << count << endl;

  return 0;
}


