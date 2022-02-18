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

void chmax(ll &x, ll y) {
    if (x < y) x = y;
}

int main() {
    ll N, W;
    cin >> N >> W;
    vector<ll> v(N);
    vector<ll> w(N);
    rep(i, N) { cin >> v[i] >> w[i]; }
    vector<vector<ll>> dp(N + 1, vector<ll>(W + 1));

    // dp[i][j]<- i番目の品物までを見た時に、重さがjの時の価値の最大値。
    rep(i, N) {
        rep(j, W + 1) {
            // 使わない時
            chmax(dp[i + 1][j], dp[i][j]);
            // 使う時
            if (j + w[i] <= W) {
                chmax(dp[i + 1][j + w[i]], dp[i][j] + v[i]);
            }
        }
    }
    ll ans = 0;
    rep(i, W + 1) { chmax(ans, dp[N][i]); }
    cout << ans << "\n";
    return 0;
}