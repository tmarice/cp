#include <iostream>
#include <queue>
#include <vector>

using namespace std;


void bfs(int start, vector<vector<int>> &conn, int n) {
	vector<int> dist(n, -1);

	queue<int> q;

	--start;
	dist[start] = 0;
	q.push(start);

	while (!q.empty()) {
		int curr = q.front();
		q.pop();

		for (int i = 0; i < conn[curr].size(); ++i)
			if (dist[conn[curr][i]] == -1) {
				dist[conn[curr][i]] = dist[curr] + 1;
				q.push(conn[curr][i]);
			}
	}

	for (int i = 0; i < n; ++i)
		if (i != start)
			if (dist[i] != -1)
				cout << dist[i] * 6 << " ";
			else
				cout << -1 << " ";

	cout << endl;
}


int main() {
	int t;

	cin >> t;

	while (t--) {
		int n, m, s;

		cin >> n >> m;

		vector<vector<int>> conn(n, vector<int>());

		for (int i = 0; i < m; ++i) {
			int x, y;
			cin >> x >> y;

			--x; --y;

			conn[x].push_back(y);
			conn[y].push_back(x);
		}

		cin >> s;

		bfs(s, conn, n);
	}

	return 0;
}
