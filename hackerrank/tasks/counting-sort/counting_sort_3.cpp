#include <iostream>
#include <string>

using namespace std;

int main() {
  int n;
  int data[100] = {0};

  cin >> n;

  while (n--) {
    int x;
    string s;
    cin >> x >> s;

    data[x]++;
  }

  int count = 0;
  int le[100] = {0};
  for (int i = 0; i < 100; ++i) {
    count += data[i];
    le[i] = count;
    cout << le[i] << " ";
  }

  cout << endl;

  return 0;
}
