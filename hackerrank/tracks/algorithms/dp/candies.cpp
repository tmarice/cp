
#include <iostream>
#include <algorithm>
using namespace std;

long long memo[100001];
long long rs[100001];
int n;

long long solve(int i) {
    if (memo[i])
        return memo[i];

    if (i == 0) {
        if (rs[i] <= rs[i+1])
            memo[i] = 1LL;
        else
            memo[i] = solve(i+1) + 1;
    }
    else if (i == n -1) {
        if (rs[i] <= rs[i-1])
            memo[i] = 1LL;
        else
            memo[i] = solve(i-1) + 1;
    }
    else {
        if (rs[i] > rs[i-1] && rs[i] > rs[i+1])
            memo[i] = max(solve(i-1), solve(i+1)) + 1;
        else if (rs[i] > rs[i-1])
            memo[i] = solve(i-1) + 1;
        else if (rs[i] > rs[i+1])
            memo[i] = solve(i+1) + 1;
        else
            memo[i] = 1LL;
    }

    return memo[i];
}


int main() {
    cin >> n;
    for (int i = 0; i < n; ++i)
        cin >> rs[i];

    long long sum = 0;
    for (int i = 0; i < n; ++i)
        sum += solve(i);

    cout << sum << endl;

    return 0;
}
