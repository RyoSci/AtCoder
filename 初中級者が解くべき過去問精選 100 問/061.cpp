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
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}
void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<vector<ll>> dp(n, vector<ll>(n, INF));
    // dp[k][i][j]<-1,2,3,...,kまでを経由地として良い状態でのiからjまでの最短距離

    rep(i, n) { dp[i][i] = 0; }

    rep(i, m) {
        ll a, b, t;
        cin >> a >> b >> t;
        a--;
        b--;
        dp[a][b] = t;
        dp[b][a] = t;
    }

    rep(k, n) {
        rep(i, n) {
            rep(j, n) {
                if (dp[i][k] == INF | dp[k][j] == INF) continue;
                chmin(dp[i][j], dp[i][k] + dp[k][j]);
            }
        }
    }

    ll ans = INF;
    rep(i, n) {
        ll worst = 0;
        rep(j, n) { chmax(worst, dp[i][j]); }
        chmin(ans, worst);
    }
    cout << ans << "\n";

    return 0;
}