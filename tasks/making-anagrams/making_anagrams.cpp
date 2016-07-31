#include <iostream>
#include <string>
#include <cmath>

using namespace std;


int main() {
  string s1, s2;
  int s1_c[30] = {0};
  int s2_c[30] = {0};

  cin >> s1 >> s2;

  for (int i = 0; i < s1.size(); ++i)
    ++s1_c[s1[i] - 'a'];

  for (int i = 0; i < s2.size(); ++i)
    ++s2_c[s2[i] - 'a'];

  int d = 0;
  for (int i = 0; i < 30; ++i)
    d += abs(s1_c[i] - s2_c[i]);

  cout << d << endl;

  return 0;
}

