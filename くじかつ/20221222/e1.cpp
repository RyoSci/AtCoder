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
#define INF (1LL << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
// #define max(x, y) ((x) > (y) ? (x) : (y))
// #define min(x, y) ((x) < (y) ? (x) : (y))
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
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> b(m);
    for (ll i = 0; i < m; i++) cin >> b[i];

    vector dp(n, vector(m, vector(2, vector(2, INF))));

    dp[0][0][0][0] = 1;
    dp[0][0][0][1] = 1;
    dp[0][0][1][0] = 1;
    if (a[0] == b[0]) dp[0][0][1][1] = 0;

    rep(i, n) {
        rep(j, m) {
            rep(k, 2) {
                rep(l, 2) {
                    if (i > 0 and j > 0) {
                        if (a[i] == b[j]) {
                            chmin(dp[i][j][1][1], dp[i - 1][j - 1][k][l]);
                        }
                        chmin(dp[i][j][0][0], dp[i - 1][j - 1][k][l] + 1);
                    }
                    if (i > 0) {
                        if (a[i] == b[j]) {
                            chmin(dp[i][j][1][1], dp[i - 1][j][k][0]);
                        }
                        chmin(dp[i][j][0][l], dp[i - 1][j][k][l] + 1);
                    }
                    if (j > 0) {
                        if (a[i] == b[j])
                            chmin(dp[i][j][1][1], dp[i][j - 1][0][l]);
                        chmin(dp[i][j][k][0], dp[i][j - 1][k][l] + 1);
                    }
                }
            }
        }
    }

    // rep(i, n) rep(j, m) {
    //     for (auto a : dp[i][j]) cout << a << " ";
    //     cout << endl;
    // }
    ll ans = INF;
    rep(i, 2) rep(j, 2) ans = min(ans, dp[n - 1][m - 1][i][j]);
    cout << ans << "\n";

    return 0;
}