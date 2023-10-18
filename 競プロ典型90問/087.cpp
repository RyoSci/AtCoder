// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
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
using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

ll n, p, k;
vector<vector<ll>> a(40, vector<ll>(40));

ll f(ll x) {
    vector<vector<ll>> dp = a;
    rep(i, n) rep(j, n) {
        if (dp[i][j] == -1) dp[i][j] = x;
    }

    rep(k, n) rep(i, n) rep(j, n) {
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
    }

    ll res = 0;
    rep(i, n - 1) rep_s(j, i + 1, n) {
        if (dp[i][j] <= p) res++;
    }
    return res;
}

int main() {
    cin >> n >> p >> k;

    rep(i, n) rep(j, n) cin >> a[i][j];

    // k以下
    ll ng = 0;
    ll ok = INF;
    if (f(ok) > k) {
        cout << 0 << "\n";
        return 0;
    }
    while (ng + 1 < ok) {
        ll mid = (ok + ng) / 2;
        if (f(mid) <= k)
            ok = mid;
        else
            ng = mid;
    }

    // k以上
    ll ok1 = 0;
    ll ng1 = INF;
    // if (f(ng1) > k) {
    //     cout << 0 << "\n";
    //     return 0;
    // }
    while (ok1 + 1 < ng1) {
        ll mid = (ok1 + ng1) / 2;
        if (f(mid) >= k)
            ok1 = mid;
        else
            ng1 = mid;
    }

    if (ok1 == INF - 1) {
        cout << "Infinity"
             << "\n";
    } else {
        cout << ok1 - ok + 1 << "\n";
    }

    return 0;
}