
#include <iostream>
#include <string>
using namespace std;


typedef long long ll;
const int MOD = 1000000007;


int main() {
  string s;

  cin >> s;

  ll prev = 0;
  ll out = 0;
  ll a;

  for (int i = 0; i < s.size(); ++i) {
    a = ((prev * 10) % MOD + ((s[i]-'0') * (i + 1)) % MOD) % MOD;
    out = (out + a % MOD) % MOD;
    prev = a;
  }

  cout << out << endl;

  return 0;
}


