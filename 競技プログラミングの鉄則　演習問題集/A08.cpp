// #define _GLIBCXX_DEBUG
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
using lli = long long;
// using mint = modint1000000007;
using mint = modint998244353;
// #define MOD 1000000007
#define MOD 998244353
#define INF (1LL << 60)
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
    ll h, w;
    cin >> h >> w;
    vector x(h + 1, vector(w + 1, 0ll));
    rep(i, h) rep(j, w) cin >> x[i + 1][j + 1];

    rep(i, h) rep(j, w) x[i + 1][j + 1] += x[i + 1][j] + x[i][j + 1] - x[i][j];

    ll q;
    cin >> q;
    rep(i, q) {
        ll a, b, c, d;
        cin >> a >> b >> c >> d;
        a--;
        b--;
        ll ans = x[c][d] - x[c][b] - x[a][d] + x[a][b];
        cout << ans << "\n";
    }
    return 0;
}