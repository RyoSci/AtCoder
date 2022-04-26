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
    ll n;
    cin >> n;
    vector<vector<ll>> d(n + 1, vector<ll>(n + 1, 0));
    rep(i, n) rep(j, n) cin >> d[i + 1][j + 1];

    rep(i, n) rep(j, n) {
        d[i + 1][j + 1] += d[i + 1][j] + d[i][j + 1] - d[i][j];
    }

    vector<ll> res(n * n + 10, 0);
    rep_s(i, 1, n + 1) rep_s(j, 1, n + 1) {
        rep_s(ii, i, n + 1) rep_s(jj, j, n + 1) {
            ll area = (ii - i + 1) * (jj - j + 1);
            ll score =
                d[ii][jj] - d[ii][j - 1] - d[i - 1][jj] + d[i - 1][j - 1];
            res[area] = max(res[area], score);
        }
    }

    rep(i, n * n) res[i + 1] = max(res[i + 1], res[i]);

    ll q;
    cin >> q;
    rep(i, q) {
        ll p;
        cin >> p;
        cout << res[p] << "\n";
    }
    return 0;
}