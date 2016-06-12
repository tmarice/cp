#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


typedef struct {
  int pos, rating, min, given;
} Emp;


int sort_fn(Emp a, Emp b) {
  return a.rating < b.rating;
}

int n;
vector<Emp> emp;
vector<Emp> emp_sort;

long long sum;

void assign_stocks(int pos) {
  int max_given = 0;

  for (int i = max(0, pos - 10); i < min(n, pos + 11); ++i)
    if (emp[i].given)
      if (emp[i].rating < emp[pos].rating)
        if (emp[i].given > max_given)
          max_given = emp[i].given;

  emp[pos].given = max(max_given + 1, emp[pos].min);

  sum += emp[pos].given;
}

int main() {

  cin >> n;

  int x;
  for (int i = 0; i < n; ++i) {
    Emp e;
    e.given = 0;
    e.pos = i;
    cin >> e.rating;
    emp.push_back(e);
    emp_sort.push_back(e);
  }
  for (int i = 0; i < n; ++i)
    cin >> emp[i].min;

  sort(emp_sort.begin(), emp_sort.end(), sort_fn);

  for (int i = 0; i < emp_sort.size(); ++i)
    assign_stocks(emp_sort[i].pos);

  /*  
  for (int i = 0; i < emp.size(); ++i)
    cout << emp[i].rating << " given " << emp[i].given << endl; 
  */

  cout << sum << endl;

  return 0;

}








