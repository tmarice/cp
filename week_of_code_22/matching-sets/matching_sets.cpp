#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


typedef long long ll;

int main() {
	int n;
	vector<ll> a, b;

	cin >> n;

	ll x;
	for (int i = 0; i < n; ++i) {
		cin >> x;
		a.push_back(x);
	}
	for (int i = 0; i < n; ++i) {
		cin >> x;
		b.push_back(x);
	}

	sort(a.begin(), a.end());
	sort(b.begin(), b.end());

	ll sum_sig = 0;
	ll sum_abs = 0;

	for (int i = 0; i < n; ++i) {
		sum_sig += a[i] - b[i];
		sum_abs += abs(a[i] - b[i]);
	}

	if (sum_sig == 0)
		cout << sum_abs / 2 << endl;
	else
		cout << -1 << endl;

	return 0;
}

