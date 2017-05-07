
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

const int INF = 1000000000;

int memo[100001] = {-1};
vector<int> graph[100001];
int burnout[100001];


int solve(int node) {
  if (graph[node].size() == 0)
    return burnout[node];

  if (memo[node] != -1)
    return memo[node];

  // send none to course
  // only possible if neither the node or its children are burned out
  int sum_zero = 0;
  int burned_out_children = 0;
  for (auto i: graph[node]) {
    if (burnout[i]) {
      burned_out_children = 1;
      break;
    }
    else {
      sum_zero += solve(i);
    }
  }
  sum_zero = !burnout[node] && !burned_out_children ? sum_zero : INF;

  // send current node to course
  int sum_first = 1;
  for (auto i: graph[node])
    for (auto j: graph[node])
      sum_first += solve(j);

  // send only unhappy children
  int sum_second = 0;
  for (auto i: graph[node]) {
    if (burnout[i]) {
      sum_second += 1;

      for (auto j: graph[i])
        for (auto k: graph[j])
          sum_second += solve(k);
    }
    else {
      sum_second += solve(i);
    }
  }
  
  return memo[node] = min(min(sum_zero, sum_first), sum_second);
}

int main() {
  int n, h, s;
  cin >> n;

  for (int i = 1; i < n; ++i) {
    cin >> s >> h;

    graph[s].push_back(i);
    burnout[i] = !h;
  }

  cout << solve(0) << endl;

  return 0;
}

