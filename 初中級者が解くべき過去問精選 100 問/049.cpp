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

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll v, e;
    cin >> v >> e;

    vector<vector<ll>> g(v, vector<ll>(v, INF));
    rep(i, e) {
        ll s, t, d;
        cin >> s >> t >> d;
        g[s][t] = d;
    }

    vector<vector<ll>> dp(1 << v, vector<ll>(v, INF));
    // ハミルトン閉路を求めるためどこからスタートしても同じコストのため
    dp[0][0] = 0;

    rep(i, 1 << v) {
        rep(t, v) {
            rep(s, v) {
                // iにsが含まれていない場合はスキップ1、i=0の時はbitが立っていないので個別に対応
                if (i != 0 && !(i >> s & 1)) continue;
                // これがないと二回以上通ることになり、ハミルトン閉路にならない
                if (!(i & (1 << t))) {
                    chmin(dp[i | 1 << t][t], dp[i][s] + g[s][t]);
                }
            }
        }
    }

    if (dp[(1 << v) - 1][0] == INF)
        cout << -1 << "\n";
    else
        cout << dp[(1 << v) - 1][0] << "\n";

    return 0;
}