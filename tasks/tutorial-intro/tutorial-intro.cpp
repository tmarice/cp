#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int v, n;
  vector<int> numbers;

  cin >> v >> n;

  int x;
  for (int i = 0; i < n; ++i) {
    cin >> x;
    numbers.push_back(x);
  }

  auto low = lower_bound(numbers.begin(), numbers.end(), v);
  auto up = upper_bound(numbers.begin(), numbers.end(), v);

  cout << low - numbers.begin() << endl;

  return 0;
}
