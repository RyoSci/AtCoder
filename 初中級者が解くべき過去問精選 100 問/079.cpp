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
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n, m, q;
    cin >> n >> m >> q;
    vector<vector<ll>> f(n + 1, vector<ll>(n + 1, 0));
    rep(i, m) {
        ll l, r;
        cin >> l >> r;
        f[l][r]++;
    }
    rep(i, n) {
        rep_s(j, i + 1, n + 1) { f[i][j] += f[i][j - 1]; }
    }

    rep(j, n + 1) {
        rep_r(i, n, 0) { f[i - 1][j] += f[i][j]; }
    }

    rep(i, q) {
        ll p, q;
        cin >> p >> q;
        cout << f[p][q] << "\n";
    }
    rep(i, n + 1) {
        for (auto a : f[i]) cout << a << " ";
        cout << endl;
    }
    return 0;
}