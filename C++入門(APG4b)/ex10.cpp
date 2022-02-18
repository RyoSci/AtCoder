#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  // ここにプログラムを追記
  int counter = 0;
  cout << "A:";
  while (counter < A) {
      cout << "]";
      counter++;
  }
  cout << endl << "B:";

  counter = 0;
  while (counter < B) {
      cout << "]";
      counter++;
  }
  cout << endl;
}
