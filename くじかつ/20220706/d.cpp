#define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
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
using mint = modint1000000007;
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

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}
int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> a(m), b(m), c(m);
    for (ll i = 0; i < m; i++) cin >> a[i] >> b[i] >> c[i];
    vector<vector<ll>> dp(n, vector<ll>(n, INF));
    rep(i, m) { chmin(dp[a[i] - 1][b[i] - 1], c[i]); }
    rep(i, n) dp[i][i] = 0;

    ll ans = 0;
    rep(k, n) rep(i, n) rep(j, n) {
        chmin(dp[i][j], dp[i][k] + dp[k][j]);
        if (dp[i][j] != INF) ans += dp[i][j];
    }
    cout << ans << "\n";
    return 0;
}