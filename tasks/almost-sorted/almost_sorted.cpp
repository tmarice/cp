#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
  vector<int> t1, t2;
  vector<int> diffs;
  int n;

  cin >> n;

  int x;
  for (int i = 0; i < n; ++i) {
    cin >> x;

    t1.push_back(x);
    t2.push_back(x);
  }

  sort(t1.begin(), t1.end());

  for (int i = 0; i < n; ++i)
    if (t1[i] != t2[i])
      diffs.push_back(i);

  if (diffs.size() == 0) {
    cout << "yes" << endl;
  }
  else if (diffs.size() == 2) {
    cout << "yes" << endl << "swap " << diffs[0] + 1 << " " << diffs[1] + 1 << endl;
  }
  else {
    int first = diffs[0];
    int last = diffs[diffs.size() - 1];

    //cout << first << " " << last << endl;
    for (int i = 0; i <= (last - first) / 2; ++i)
      swap(t2[first + i], t2[last - i]);

    /*
    for (int i = 0; i < n; ++i) {
      cout << t1[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < n; ++i) {
      cout << t2[i] << " ";
    }
    cout << endl;
    */

    for (int i = diffs[0]; i <= last; ++i)
      if (t1[i] != t2[i]) {
        cout << "no" << endl;
        return 0;
      }
    cout << "yes" << endl << "reverse " << diffs[0] + 1 << " " << last + 1 << endl;
  }

  return 0;
}
