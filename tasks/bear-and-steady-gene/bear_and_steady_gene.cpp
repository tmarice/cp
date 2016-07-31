#include <iostream>
#include <string>
#include <map>

using namespace std;


int main() {
  int n;
  string s;
  map<char, int> m = {{'A', 0}, {'C', 1}, {'G', 2}, {'T', 3}};
  int orig[4] = {0};

  cin >> n >> s;

  for (int i = 0; i < s.size(); ++i)
    ++orig[m[s[i]]];

  int goal[4] = {0};

  for (int i = 0; i < 4; ++i)
    if (orig[i] > n / 4)
      goal[i] = orig[i] - n/4;

  int count[4] = {0};
  int min_index, max_index; // range = [min_index, max_index>
  for (max_index = 0; max_index < s.size(); ++max_index) {

    /*
    cout << max_index << endl;
    for (int i = 0; i < 4; ++i)
      cout << goal[i] << " " << count[i] << endl;
    */

    // check if goal <= count
    int g = 0;
    for (int i = 0; i < 4; ++i)
      if (count[i] >= goal[i])
        ++g;
    if (g == 4)
      break;
      
    // if it isn't, add current character to range
    ++count[m[s[max_index]]];
  }

  for (min_index = 0; min_index <= max_index; min_index++) {
    // take away current char
    --count[m[s[min_index]]];

    // check if we broke anything with this
    int g = 0;
    for (int i = 0; i < 4; ++i)
      if (count[i] >= goal[i])
        ++g;
    if (g != 4) {
      break;
    }

    /*
    cout << min_index << endl;
    for (int i = 0; i < 4; ++i)
      cout << goal[i] << " " << count[i] << endl;
    */
  }

  cout << max_index - min_index << endl;
  /*
  for (int i = min_index; i < max_index; ++i)
    cout << s[i];
  cout << endl;
  */

  return 0;
}






  
