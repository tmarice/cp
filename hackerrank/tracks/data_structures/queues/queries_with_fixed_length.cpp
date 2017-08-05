#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;

template <typename T>
class MaxQueue {
  private:
    deque<T> items;
    deque<T> max;

  public:
    void append(T x) {
      items.push_back(x);

      while (!max.empty() && max.back() < x)
        max.pop_back();

      max.push_back(x);
    }

    T pop() {
      T x = items.front();
      items.pop_front();

      if (x == max.front())
        max.pop_front();

      return x;
    }

    T get_max() {
      return max.front();
    }
};


int main() {
  int n, q;
  vector<int> a;

  cin >> n >> q;

  int x;
  for (int i = 0; i < n; ++i) {
    cin >> x;
    a.push_back(x);
  }

  int d;
  for (int i = 0; i < q; ++i) {
    cin >> d;
    MaxQueue<int> queue;

    for (int j = 0; j < d; ++j) {
      queue.append(a[j]);
    }

    int m = queue.get_max();
    for (int j = d; j < n; ++j) {
      queue.pop();
      queue.append(a[j]);
      m = min(m, queue.get_max());
    }

    cout << m << endl;
  }

  return 0;
}
