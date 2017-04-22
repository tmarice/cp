#include <iostream>
#include <algorithm>

using namespace std;

const int INF = 1000000000;

// [offer type][day][price, min, max stay]
int offers[200][300][3];
// [# nights][day]
int mins[301][300];

int main() {
  int n, m, q;
  cin >> n >> m >> q;

  int x;
  for (int k = 0; k < 3; ++k) {
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        cin >> x;
        offers[i][j][k] = x;
      }
    }
  }

  for (int i = 0; i < n; ++i) {
    for (int k = 0; k <= n; ++k) {
      int best = INF;

      for (int j = 0; j < m; ++j) {
        if (offers[j][i][0] > 0 && k >= offers[j][i][1] && k <= offers[j][i][2])
          best = min(best, offers[j][i][0]);
      }

      mins[k][i] = best;
    }
  }

  for (int i = 0; i < q; ++i) {
    int c, l;
    cin >> c >> l;

    --c;
    int output = 0;

    for (int i = c; i < c+l; ++i)
      if (mins[l][i] == INF) {
        output = -1;
        break;
      }
      else {
        output += mins[l][i];
      }

    cout << output << endl;
  }

  return 0;
}
