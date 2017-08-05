/*
 * Idea:
 * Sort the mandragoras by health. Then try to eat mandragoras in that order,
 * and check if experience gained from battling the others is increasing. When
 * it starts to drop, it's time to stop eating.
 *
 * This isn't DP, but greedy problem, because strength gained does not depend on
 * mandragora health. If it did, greedy would not work.
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


typedef long long ll;


int main() {
  int t;

  cin >> t;

  while (t--) {
    int n;
    vector<int> h;
    ll sum = 0;

    cin >> n;

    for (int i = 0; i < n; ++i) {
      int x;
      cin >> x;

      sum += x;
      h.push_back(x);
    }

    sort(h.begin(), h.end());

    ll max = sum;
    for (int i = 1; i < h.size(); ++i) {
      sum -= h[i - 1];
      ll p = sum * (i + 1);

      if (p > max)
        max = p;
      else
        break;
    }

    cout << max << endl;
  }

  return 0;
}

