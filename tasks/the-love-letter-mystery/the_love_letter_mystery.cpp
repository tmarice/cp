#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
	int t;

	cin >> t;

	while (t--) {
		string s;
		int total = 0;

		cin >> s;

		for (int i = 0, j = s.size() - 1; i < j; i++, j--)
			total += abs(s[i] - s[j]);

		cout << total << endl;
	}

	return 0;
}





