#include <iostream>

using namespace std;


int main() {
	int q;

	cin >> q;

	while (q--) {
		int n;

		cin >> n;

		if (n % 2 == 1)
			cout << "No" << endl;
		else
			cout << "Yes" << endl;
	}

	return 0;
}
