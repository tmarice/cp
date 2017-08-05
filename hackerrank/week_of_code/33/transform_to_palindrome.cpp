
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <stack>
#include <cstring>
#include <algorithm>
using namespace std;

int pool[100001];
int memo[1001][1001];
unordered_map<int, vector<int>> trans;
vector<int> s;
int visited[100001];


void flood_fill(int n) {
    int t = 0;

    for (int i = 1; i <= n; ++i) {
        if (!visited[i]) {
            stack<int> st;
            st.push(i);
            visited[i] = 1;
            int cur;

            while (!st.empty()) {
                cur = st.top();
                st.pop();
                pool[cur] = t;

                for (int j = 0; j < trans[cur].size(); ++j)
                    if (!visited[trans[cur][j]]) {
                        visited[trans[cur][j]] = 1;
                        st.push(trans[cur][j]);
                    }
            }

            t += 1;
        }
    }
}


int transform(int first, int last) {
    if (first >= last)
        return 0;
    else if (memo[first][last] != -1)
        return memo[first][last];
    else {
        if (pool[s[first]] == pool[s[last]])
            return memo[first][last] = transform(first + 1, last - 1);
        else
            return memo[first][last] = 1 + min(transform(first + 1, last), transform(first, last - 1));
    }
}

int main() {
    int n, k, m, a, b;
    cin >> n >> k >> m;

    for (int i = 0; i < k; ++i) {
        cin >> a >> b;
        trans[a].push_back(b);
        trans[b].push_back(a);
    }

    flood_fill(n);

    for (int i = 0; i < m; ++i) {
        cin >> a;
        s.push_back(a);
    }

    memset(memo, -1, sizeof(memo));
    cout << m - transform(0, m-1) << endl;

    return 0;
}
