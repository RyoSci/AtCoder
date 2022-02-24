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
#define _GLIBCXX_DEBUG

void chmin(ll& x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll v, e;
    cin >> v >> e;
    vector<vector<ll>> dp(v, vector<ll>(v, INF));
    rep(i, v) { dp[i][i] = 0; }
    rep(i, e) {
        ll s, t, d;
        cin >> s >> t >> d;
        dp[s][t] = d;
    }

    rep(k, v) {
        rep(i, v) {
            if (dp[i][k] == INF) continue;
            rep(j, v) {
                if (dp[k][j] == INF) continue;
                chmin(dp[i][j], dp[i][k] + dp[k][j]);
            }
        }
    }
    bool has_neg_cycle = false;
    rep(i, v) {
        if (dp[i][i] < 0) has_neg_cycle = true;
    }
    if (has_neg_cycle)
        cout << "NEGATIVE CYCLE" << endl;
    else {
        rep(i, v) {
            rep(j, v - 1) {
                if (dp[i][j] == INF)
                    cout << "INF"
                         << " ";
                else
                    cout << dp[i][j] << " ";
            }
            if (dp[i][v - 1] == INF)
                cout << "INF";
            else
                cout << dp[i][v - 1];
            cout << endl;
        }
    }
    return 0;
}