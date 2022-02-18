#include <algorithm>
#include <atcoder/all>
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
using namespace atcoder;
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
// #include <atcoder/modint>
using mint = modint1000000007;
// using mint = modint998244353;

bool f(Int a, Int s) {
    rep(i, 100) {
        if (s == 0) return a == 0;
        rep(x, 2) {
            rep(y, 2) {
                if (x == 1 && y == 0) continue;
                if ((x & y) != (a & 1)) continue;
                if ((s - x - y) < 0) continue;
                if ((s - x - y) & 1 != 0) continue;
                if (f(a >> 1, (s - x - y) >> 1)) return true;
            }
        }
        return false;
    }
}

int main() {
    Int t;
    cin >> t;
    rep(i, t) {
        Int a, s;
        cin >> a >> s;
        if (f(a, s))
            cout << "Yes"
                 << "\n";
        else
            cout << "No"
                 << "\n";
    }
    return 0;
}