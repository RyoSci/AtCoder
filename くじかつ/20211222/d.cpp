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

int main() {
    Int n;
    cin >> n;
    vector<Int> a(n);
    for (Int i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());
    Int max_a = a[n - 1];
    Int res = 0;
    Int k = 0;
    rep(i, n - 1) {
        Int tmp = min(max_a - a[i], a[i]);
        if (tmp >= res) {
            res = tmp;
            k = a[i];
        }
    }
    cout << max_a << " " << k << "\n";
    return 0;
}