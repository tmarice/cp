#include <iostream>
#include <vector>
#include <utility>
using namespace std;

int p;
double r;
int t;
int thr;

int sum_orig;

vector<int> s;
vector<int> s_orig;
vector<pair<double, vector<int>>> bests;


double get_income() {
  double itotal = 0;
  double x = (1 + r) / 100;

  for (int i = 0; i < t; ++i) {
    itotal += s[i] * x;
    x *= (100 - s[i]) * (1 + r) / 100;
  }

  return itotal * p;
}

void insert_best(double sum) {
  if (sum > bests[0].first) {
    bests[2] = bests[1];
    bests[1] = bests[0];
    bests[0] = make_pair(sum, s);
  }
  else if (sum > bests[1].first) {
    bests[2] = bests[1];
    bests[1] = make_pair(sum, s);
  }
  else if (sum > bests[2].first) {
    bests[2] = make_pair(sum, s);
  }
}

void get_good_combinations(int pos) {
  if (pos == t) {
    int sum = 0;
    for (int x: s)
      sum += x;

    if (sum != sum_orig)
      return;

    insert_best(get_income());
    /*
    for (int i = 0; i < s.size(); ++i) 
      cout << s[i] << " ";
    cout << " - " << get_income() << endl;
    */

    return;
  }

  for (s[pos] = max(0, s_orig[pos] - thr); s[pos] <= min(99, s_orig[pos] + thr); ++s[pos]) {
    /*
    if (s[pos] == s_orig[pos])
      continue;
      */

    get_good_combinations(pos + 1);
  }
}







int main() {
  cin >> p >> r >> t >> thr;

  cout.setf(ios::fixed, ios::floatfield);
  cout.precision(3);

  r /= 100;

  int x;
  for (int i = 0; i < t; ++i) {
    cin >> x;
    s.push_back(x);
    s_orig.push_back(x);
    sum_orig += x;
  }

  bests.push_back(make_pair(0, vector<int>(t, 0)));
  bests.push_back(make_pair(0, vector<int>(t, 0)));
  bests.push_back(make_pair(0, vector<int>(t, 0)));

  cout << get_income() << endl;

  get_good_combinations(0);

  for (int i = 0; i < 3; ++i) {
    cout << bests[i].first << " -";
    for (int x: bests[i].second)
      cout << " " << x;
    cout << endl;
  }

  return 0;
}



