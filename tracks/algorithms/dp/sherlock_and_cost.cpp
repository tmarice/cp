
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int memo[100000][2];
int bs[100000];


int solve(int i, int last) {
    if (i <= 0)
        return 0;

    if (memo[i][last] != -1)
        return memo[i][last];

    return memo[i][last] = max(
            solve(i-1, last) + (last == 0 ? 0 : abs(bs[i-1] - bs[i])),
            solve(i-1, !last) + (last == 0 ? abs(bs[i-1] - 1) : abs(bs[i] - 1)));
}

int main() {
    int t, n;

    cin >> t;

    while (t--) {
        cin >> n;

        for (int i = 0; i < n; ++i)
            cin >> bs[i];

        memset(memo, -1, sizeof(memo));

        cout << max(solve(n-1, 0), solve(n-1, 1)) << endl;
    }

    return 0;
}





