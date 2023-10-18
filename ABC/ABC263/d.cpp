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
    ll n, l, r;
    cin >> n >> l >> r;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<vector<ll>> dp(n + 1, vector<ll>(2, INF));
    dp[0][0] = dp[0][1] = 0;
    rep(i, n) {
        chmin(dp[i + 1][0], dp[i][0] + a[i]);
        if (dp[i][1] == INF) continue;
        chmin(dp[i + 1][0], dp[i][1] + l);
        chmin(dp[i + 1][1], dp[i][1] + l);
    }

    ll ans = min(dp[n][0], dp[n][1]);
    rep_r(i, n - 1, -1) {
        ll tmp = r * (n - i);
        ans = min(ans, tmp + min(dp[i][0], dp[i][1]));
    }

    cout << ans << "\n";
    // rep(i, n + 1) {
    //     for (auto a : dp[i]) cout << a << " ";
    //     cout << endl;
    // }
    return 0;
}