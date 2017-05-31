
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;


int graph[501][501];

int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};


int main() {
    int t;

    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;

        int init_max = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                cin >> graph[i][j];
                init_max = max(init_max, graph[i][j]);
            }

        queue<pair<pair<int, int>, int>> q;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (graph[i][j] == init_max) {
                    q.push(make_pair(make_pair(i, j), 0));
                    graph[i][j] = -1;
                }

        pair<int, int> coords;
        int cur_i, cur_j, dist, neigh_i, neigh_j;
        int out = 0;
        while (q.size() != 0) {
            coords = q.front().first;
            cur_i = coords.first;
            cur_j = coords.second;
            dist = q.front().second;
            q.pop();

            out = max(out, dist);

            for (int i = 0; i < 8; ++i) {
                neigh_i = cur_i + dy[i];
                neigh_j = cur_j + dx[i];

                if (neigh_i >= 0 and neigh_i < n and neigh_j >= 0 and neigh_j < m)
                    if (graph[neigh_i][neigh_j] != -1) {
                        graph[neigh_i][neigh_j] = -1;
                        q.push(make_pair(make_pair(neigh_i, neigh_j), dist + 1));
                    }
            }
        }

        cout << out << endl;
    }

    return 0;
}
