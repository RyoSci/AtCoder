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

void chmin(ll& x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> a(m), b(m);
    vector<vector<ll>> c(m);

    rep(i, m) {
        cin >> a[i] >> b[i];
        ll ci;
        rep(j, b[i]) {
            cin >> ci;
            c[i].push_back(ci);
        }
    }

    vector<vector<ll>> dp(m + 1, vector<ll>(1 << n, INF));
    dp[0][0] = 0;
    rep(i, m) {
        rep(j, 1 << n) {
            ll tmp = 0;
            rep(k, b[i]) { tmp = tmp | (1 << c[i][k] - 1); }
            chmin(dp[i + 1][j | tmp], dp[i][j] + a[i]);
            chmin(dp[i + 1][j], dp[i][j]);
        }
    }

    if (dp[m][(1 << n) - 1] == INF)
        cout << -1 << "\n";
    else
        cout << dp[m][(1 << n) - 1] << "\n";

    // rep(i, m + 1) {
    //     for (ll x : dp[i]) {
    //         if (x == INF) x = -1;
    //         cout << x << " ";
    //     }
    //     cout << endl;
    // }
    return 0;
}