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

void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

ll dp[55][10005][55];

int main() {
    ll w;
    cin >> w;
    ll n, K;
    cin >> n >> K;
    vector<ll> a(n), b(n);
    for (ll i = 0; i < n; i++) cin >> a[i] >> b[i];

    // dp[i][j][k]:=i番目までのスクリーンショットの中からk枚使って幅の合計がjとなるときの重要度の最大値
    rep(i, n) rep(j, w + 1) rep(k, K + 1) {
        // 使う
        if (j + a[i] <= w && k + 1 <= K)
            chmax(dp[i + 1][j + a[i]][k + 1], dp[i][j][k] + b[i]);
        // 使わない
        chmax(dp[i + 1][j][k], dp[i][j][k]);
    }
    ll ans = 0;
    rep(j, w + 1) rep(k, K + 1) chmax(ans, dp[n][j][k]);
    cout << ans << "\n";
    return 0;
}