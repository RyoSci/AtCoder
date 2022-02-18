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

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<vector<ll>> dp(n, vector<ll>(21));
    dp[1][a[0]] = 1;

    // dp[i][j]<- i番目までの数値を見て、合計がjとなる時の通り数

    rep_s(i, 1, n - 1) {
        rep(j, 21) {
            // 足し算
            if (j + a[i] <= 20) {
                dp[i + 1][j + a[i]] += dp[i][j];
            }

            // 引き算
            if (j - a[i] >= 0) {
                dp[i + 1][j - a[i]] += dp[i][j];
            }
        }
    }
    cout << dp[n - 1][a[n - 1]] << "\n";
    rep(i, n) {
        for (ll a : dp[i]) cout << a << " ";
        cout << endl;
    }
    return 0;
}