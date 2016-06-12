#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

class Entry {
  public:
  ll idx, gain, used;

  Entry(ll idx, ll gain, int used): idx(idx), gain(gain), used(used) {}

};

int sort_fn(Entry *a, Entry *b) {
  return a->gain > b->gain;
}

int main() {
  ll n, m, k;
  vector<Entry*> secs;

  cin >> n >> m >> k;

  ll prc, prb;
  for (int i = 0; i < n; ++i) {
    cin >> prc >> prb;

    secs.push_back(new Entry(i, prc * prb, 0));
    secs.push_back(new Entry(i, prc * 100, 1));
  }

  sort(secs.begin(), secs.end(), sort_fn);

  ull sum = 0;
  int taken[n];
  memset(taken, 0, sizeof(taken));

  for (int first = 0; first < secs.size(), m; ++first) {
    if (taken[secs[first]->idx]) 
      continue;

    if (secs[first]->used) {
      if (!k)
        continue;
      else
        --k;
    }

    sum += secs[first]->gain;
    taken[secs[first]->idx] = 1;
    --m;
  }

  cout << sum << endl;

  return 0;
}
