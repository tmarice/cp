#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  while (n--) {
    double usd_eur, eur_gbp, gbp_usd;

    cin >> usd_eur >> eur_gbp >> gbp_usd;

    int money= 100000 / usd_eur / eur_gbp / gbp_usd;

    cout << int(max(money- 100000, 0)) << endl;
  }

  return 0;
}
