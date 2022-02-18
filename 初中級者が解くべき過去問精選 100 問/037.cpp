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

void chmin(ll& x, ll y) {
    if (y < x) x = y;
    return;
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> c(m);
    for (ll i = 0; i < m; i++) cin >> c[i];

    vector<vector<ll>> dp(m + 1, vector<ll>(n + 1, INF));
    dp[0][0] = 0;
    // dp[i][j]<-i番目までのコインを見た時に、j円となるコインの枚数の最小枚数。
    rep(i, m) {
        rep(j, n + 1) {
            // 使わない場合
            chmin(dp[i + 1][j], dp[i][j]);
            // 使う場合
            if (j + c[i] <= n) {
                chmin(dp[i + 1][j + c[i]], dp[i][j + c[i]] + 1);
                chmin(dp[i + 1][j + c[i]], dp[i + 1][j] + 1);
            }
        }
    }
    cout << dp[m][n] << "\n";
    return 0;
}