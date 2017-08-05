
#include <iostream>
#include <bitset>
#include <unordered_map>
using namespace std;


typedef long long ll;

ll xs[20];
int n;
unordered_map<unsigned long, ll> memo;


ll solve(bitset<20> &state, ll cur_sum) {
  unsigned long sul = state.to_ulong();
  if (memo.count(sul))
    return memo[sul];

  if (state.count() == 1)
    for (int i = 0; i < n; ++i)
      if (state.test(i))
        return memo[sul] = 0;

  ll score = 0;
  ll cur_score, run_sum;

  for (int i = 0; i < n; ++i)
    if (state.test(i)) {
      state.flip(i);
      run_sum = cur_sum - xs[i];
      cur_score = solve(state, run_sum);
      state.flip(i);

      if (cur_score + run_sum % xs[i] > score)
        score = cur_score + run_sum % xs[i];
    }

  return memo[sul] = score;
}


int main() {
  cin >> n;
  ll sum = 0;

  for (int i = 0; i < n; ++i) {
    cin >> xs[i];
    sum += xs[i];
  }

  bitset<20> state;
  for (int i = 0; i < n; ++i)
    state.set(i);

  cout << solve(state, sum) << endl;

  return 0;
}



