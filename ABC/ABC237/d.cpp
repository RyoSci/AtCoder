#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (Int i = 0; i < n; i++)
#define rep_r(i, k, n) for (Int i = k; i > n; i--)
#define rep_s(i, k, n) for (Int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)
#include <list>
#include <numeric>

int main() {
    Int n;
    cin >> n;
    string s;
    cin >> s;
    list<Int> lst;
    lst.push_front(0);
    auto iter = lst.begin();
    rep(i, n) {
        cout << distance(lst.begin(), iter) << "\n";
        if (s[i] == 'L') {
            iter = lst.insert(iter, i + 1);
        } else {
            iter++;
            iter = lst.insert(iter, i + 1);
        }
        for (Int a : lst) cout << a << " ";
        cout << endl;
    }

    for (Int a : lst) cout << a << " ";
    cout << endl;

    return 0;
}