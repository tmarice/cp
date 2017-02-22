#include <iostream>
#include <iomanip>

using namespace std;


int main() {
	int x, y, a, b;

	cin >> x >> y >> a >> b;

	double n = double((y*a - x*b)) / (b*b + a*a);
	double k = (x + n*b) / a;

	cout << fixed << setprecision(12) << k << endl << n << endl;

	return 0;
}
