
#include <iostream>
#include <set>
#include <cstring>
#include <queue>
#include <utility>
using namespace std;


int rs[10000001];

void fill_rs(int n, int g, int seed, int p) {
    for (int i = 1; i < n; ++i)
        rs[i] = (rs[i-1] * g + seed) % p;
}

int bfs(int n, int s, int t) {
    if (s == t)
        return 0;

    queue<pair<int, int>> q;
    q.push(make_pair(s, 0));
    set<int> not_visited;

    for (int i = 0; i < n; ++i)
        not_visited.insert(i);
    not_visited.erase(s);

    /* for (auto i = not_visited.begin(); i != not_visited.end(); ++i) */
    /*     cout << *i << " "; */
    /* cout << endl; */

    int cur, dist, r, r_l, r_r;
    while (q.size() != 0) {
        cur = q.front().first;
        dist = q.front().second;
        //cout << cur << " " << dist << endl;
        q.pop();

        r = rs[cur];
        r_l = (cur - r + n) % n;
        r_r = (cur + r) % n;

        //cout << r_l << " " << r_r << endl;

        if (r_l > r_r) {
            for (auto i = not_visited.lower_bound(r_l); i != not_visited.end(); ) {
                //cout << "FIRST" << " " << *i << endl;
                if (*i == t)
                    return dist + 1;
                else {
                    q.push(make_pair(*i, dist + 1));
                    not_visited.erase(i++);
                }
            }
            for (auto i = not_visited.lower_bound(0); i != not_visited.upper_bound(r_r); ) {
                //cout << "SECOND" << " " << *i << endl;
                if (*i == t)
                    return dist + 1;
                else {
                    q.push(make_pair(*i, dist + 1));
                    not_visited.erase(i++);
                }
            }
        }
        else {
            for (auto i = not_visited.lower_bound(r_l); i != not_visited.upper_bound(r_r); ) {
                //cout << "SECOND" << " " << *i << endl;
                if (*i == t)
                    return dist + 1;
                else {
                    q.push(make_pair(*i, dist + 1));
                    not_visited.erase(i++);
                }
            }
        }
    }

    return -1;
}


int main() {
    int n, s, t, g, seed, p;

    cin >> n >> s >> t >> rs[0] >> g >> seed >> p;

    if (s == t)
        cout << 0 << endl;
    else {
        fill_rs(n, g, seed, p);
        cout << bfs(n, s, t) << endl;
    }

    return 0;
}
