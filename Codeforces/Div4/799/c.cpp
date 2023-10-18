// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll t;
    cin >> t;
    rep(_, t) {
        vector<string> g(8);
        rep(i, 8) cin >> g[i];
        ll gi, gj;
        rep_s(i, 1, 7) rep_s(j, 1, 7) {
            if (g[i][j] == '#' && g[i + 1][j + 1] == '#' &&
                g[i + 1][j - 1] == '#' && g[i - 1][j + 1] == '#' &&
                g[i - 1][j - 1] == '#') {
                gi = i;
                gj = j;
                break;
            }
        }
        cout << gi + 1 << ' ' << gj + 1 << "\n";
    }
    return 0;
}