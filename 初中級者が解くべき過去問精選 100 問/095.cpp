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
// #include <atcoder/all>
// #include <atcoder/modint>
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;

int main() {
    Int a, b, k;
    cin >> a >> b >> k;
    // if (k >= a) {
    //     k -= a;
    //     a = 0;
    //     b = max(0, b - k);
    // } else {
    //     a -= k;
    // }
    // cout << a << ' ' << b << "\n";

    Int use = min(a, k);
    a = a - use;
    b = max(0, b - (k - use));
    cout << a << ' ' << b << "\n";
    return 0;
}