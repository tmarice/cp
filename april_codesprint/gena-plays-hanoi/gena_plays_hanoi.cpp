#include <iostream>
#include <bitset>
#include <queue>
#include <unordered_set>

typedef long long LL;
#define mp make_pair

using namespace std;

unordered_set<LL> visited;

int main() {
  int n;
  LL h = 0;

  cin >> n;

  // construct goal bitvector - all plates on first rod
  LL goal = 0;
  for (int i = 0; i < n; ++i)
    goal |= 1 << i;

  int t;
  for (int i = 0; i < n; ++i) {
    cin >> t;
    h |= 1LL << ((t-1) * 10 + i);
  }

  queue<pair<LL, int>> q;
  q.push(mp(h, 0));

  while (!q.empty()) {
    LL cur = q.front().first;
    int cur_dist = q.front().second;
    visited.insert(cur);
    //cout << bitset<40>(cur) << " : " << cur_dist << endl;
    q.pop();

    // find smallest plate on each rod - that's the top
    int cur_plates[] = {-1, -1, -1, -1};
    for (int i = 0; i < 4; ++i) 
      for (int j = 9; j >= 0; --j) 
        if ((cur >> (i * 10 + j)) & 1)
          cur_plates[i] = j;

    //cout << cur_plates[0] << " " << cur_plates[1] << " " << cur_plates[2] << " " << cur_plates[3] << endl;
           
    //for every rod combination (a,b):
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j) {
        //  check if move i -> j is possible - if not, continue
        if (cur_plates[i] >= 0 && cur_plates[i] >= cur_plates[j])
          continue;

        //  encode a->b move to bitvector bv
        LL next = h;
        next ^= 1LL << (i * 10 + cur_plates[i]);
        next ^= 1LL << (j * 10 + cur_plates[i]);

        //cout << bitset<40>(next) << endl;

        //  check if it is already visited - if not, continue
        if (visited.count(next))
          continue;
        //  check if bv is goal position 
        if (next == goal) {
          // if it is, print cur_dist + 1, and break
          cout << cur_dist + 1 << endl;
          return 0;
        }

        // else, push (bv, cur_dist + 1) to queue
        q.push(mp(next, cur_dist + 1)); 
      }
  }

  return 0;
}
