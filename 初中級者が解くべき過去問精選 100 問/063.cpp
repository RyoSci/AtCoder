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

int main() {
    ll n;
    cin >> n;
    vector<vector<ll>> dp(n, vector<ll>(n, 0));
    rep(i, n) {
        rep(j, n) { cin >> dp[i][j]; }
    }
    vector<vector<ll>> cnt(n, vector<ll>(n, 0));

    bool flag = true;
    rep(k, n) {
        rep(i, n) {
            rep(j, n) {
                if (dp[i][j] == dp[i][k] + dp[k][j])
                    cnt[i][j]++;
                else if (dp[i][j] > dp[i][k] + dp[k][j])
                    flag = false;
            }
        }
    }

    ll ans = 0;
    if (flag) {
        rep(i, n) {
            rep(j, n) {
                if (cnt[i][j] == 2) ans += dp[i][j];
            }
        }
        cout << ans / 2 << "\n";
    } else {
        cout << -1 << "\n";
    }
    // rep(i, n) {
    //     for (auto a : cnt[i]) cout << a << " ";
    //     cout << endl;
    // }
    return 0;
}