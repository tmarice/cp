#include <iostream>

using namespace std;

typedef long long ll;


int main() {
	ll n, m;

	cin >> n >> m;

	if (m % n == 0) {
		cout << 0 << endl;
	}
	else if (n < m) {
		cout << n - m % n << endl;
	}
	else if (n > m) {
		cout << n - m << endl;
	}

	return 0;
}
