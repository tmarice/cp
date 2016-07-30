#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


const int INF = 1000000000;


int main() {
  vector<int> numbers;
  int n;

  cin >> n;

  while (n--) {
    int x;
    cin >> x;

    numbers.push_back(x); 
  }

  sort(numbers.begin(), numbers.end());

  int min = INF;
  vector<pair<int, int>> output;

  for (int i = 0; i < numbers.size() - 1; ++i) {
    int diff = abs(numbers[i] - numbers[i + 1]);

    if (diff < min) {
      min = diff;
      output.clear();
    }

    if (diff == min) {
      output.push_back(make_pair(numbers[i], numbers[i + 1]));
    }
  }

  for (int i = 0; i < output.size(); ++i) 
    cout << output[i].first << " " << output[i].second << " ";

  cout << endl;

  return 0;

}
