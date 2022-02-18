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
#define _GLIBCXX_DEBUG

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}

ll f(ll x, ll y) { return (x - y) * (x - y); }

int main() {
    while (1) {
        ll n, m;
        cin >> n >> m;
        if (n == 0 && m == 0) return 0;
        vector<ll> c(m);
        for (ll i = 0; i < m; i++) cin >> c[i];
        vector<ll> x(n);
        for (ll i = 0; i < n; i++) cin >> x[i];
        vector<vector<ll>> dp(n + 1, vector<ll>(256, INF));

        // dp[i][j]<-i番目までの標本の符号化がjとなる時の今までのスコアの最小値
        dp[0][128] = 0;
        rep(i, n) {
            rep(j, 256) {
                if (dp[i][j] == INF) continue;
                rep(k, m) {
                    if (j + c[k] >= 255)
                        chmin(dp[i + 1][255], dp[i][j] + f(255, x[i]));
                    else if (j + c[k] <= 0)
                        chmin(dp[i + 1][0], dp[i][j] + f(0, x[i]));
                    else
                        chmin(dp[i + 1][j + c[k]],
                              dp[i][j] + f(j + c[k], x[i]));
                }
            }
        }

        ll ans = INF;
        rep(i, 256) { ans = min(ans, dp[n][i]); }
        cout << ans << "\n";
    }
    return 0;
}