#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
  int chars[30] = {0};
  string s;

  getline(cin, s);

  for (int i = 0; i < s.size(); ++i)
    chars[toupper(s[i]) - 'A']++;

  for (int i = 'A'; i <= 'Z'; ++i)
    if (chars[i - 'A'] == 0) {
      cout << "not pangram" << endl;
      return 0;
    }

  cout << "pangram" << endl;

  return 0;
}


