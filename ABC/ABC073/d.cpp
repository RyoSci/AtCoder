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

void chmin(ll &a, ll b) {
    if (a > b) a = b;
    return;
}

int main() {
    ll n, m, R;
    cin >> n >> m >> R;
    vector<ll> r(R, 0);
    rep(i, R) cin >> r[i];

    vector<vector<ll>> dp(n, vector<ll>(n, INF));
    rep(i, n) dp[i][i] = 0;
    rep(i, m) {
        ll a, b, c;
        cin >> a >> b >> c;
        a--, b--;
        chmin(dp[a][b], c);
        chmin(dp[b][a], c);
    }

    rep(k, n) rep(i, n) rep(j, n) { chmin(dp[i][j], dp[i][k] + dp[k][j]); }

    ll dis = INF;
    sort(r.begin(), r.end());
    do {
        ll tmp = 0;
        for (int i = 0; i < r.size() - 1; i++) {
            tmp += dp[r[i] - 1][r[i + 1] - 1];
        }
        if (dis > tmp) dis = tmp;
    } while (next_permutation(r.begin(), r.end()));

    cout << dis << "\n";
    return 0;
}