#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int n = 0, max = 0, cant = 0;
  vector<int> vec;
  vector<int> new_vec;

  cin >> n;
  cin >> max;


  for (int i = 0;  i< n; i++){
    int first = 0, last = 0;

    cin >> first;
    cin >> last;

    for (int j = first; j  <= last; j++){
      vec.push_back(j);
    }
  }

  for (int i = 1; i <= max; i++ ){
    bool b = false;
    for (int j = 0; j <= vec.size()-1; j++){
      if (i == vec[j]){
	b = true;
      }
    }

    if (b == false){
      new_vec.push_back(i);
      cant += 1;
    }
  }

  cout << cant << "\n";

  for (auto element: new_vec){
    cout << element << " ";
  }
}
