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
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)
// #include <atcoder/all>
// #include <atcoder/modint>
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;

void chmax(ll& x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    ll d, n;
    cin >> d >> n;
    vector<ll> t(d);
    for (ll i = 0; i < d; i++) cin >> t[i];
    vector<ll> a(n), b(n), c(n);
    for (ll i = 0; i < n; i++) cin >> a[i] >> b[i] >> c[i];

    vector<vector<ll>> dp(d, vector<ll>(n, -1));
    // dp[i][j]<-i-1番目までの日程までは服の着方が決まっていて、i番目にjの服をきた場合のスコアの最大値

    rep(j, n) {
        if (a[j] <= t[0] && t[0] <= b[j]) {
            dp[0][j] = 0;
        }
    }

    rep_s(i, 1, d) {
        rep(j, n) {
            if (dp[i - 1][j] == -1) continue;
            rep(k, n) {
                if (a[k] <= t[i] && t[i] <= b[k]) {
                    chmax(dp[i][k], dp[i - 1][j] + abs(c[j] - c[k]));
                }
            }
        }
    }
    ll ans = 0;
    rep(i, n) { ans = max(ans, dp[d - 1][i]); }
    cout << ans << "\n";
    rep(i, n) {
        for (auto a : dp[i]) cout << a << " ";
        cout << endl;
    }
    return 0;
}