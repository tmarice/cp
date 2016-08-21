#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Order {
  public:
    int t, n;

    Order(int ti, int ni): t(ti), n(ni) {}

    bool operator<(const Order& other) const {
      if (t == other.t)
        return n < other.n;
      else
        return t < other.t;
    }

};


int main() {
  int n;
  vector<Order> orders;

  cin >> n;

  int ti, di;
  for (int i = 1; i <= n; ++i) {
    cin >> ti >> di;
    orders.push_back(Order(ti + di, i));
  }

  sort(orders.begin(), orders.end());

  for (int i = 0; i < n; ++i)
    cout << orders[i].n << " ";

  cout << endl;

  return 0;
}






