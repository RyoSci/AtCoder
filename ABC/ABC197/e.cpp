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
}

void chmax(ll &x, ll y) {
    if (x < y) x = y;
}

int main() {
    ll n;
    cin >> n;
    map<ll, P> d;
    vector<ll> x(n), c(n);
    for (ll i = 0; i < n; i++) cin >> x[i] >> c[i];
    rep(i, n) {
        d[c[i]].first = INF;
        d[c[i]].second = -INF;
    }

    rep(i, n) {
        chmin(d[c[i]].first, x[i]);
        chmax(d[c[i]].second, x[i]);
    }

    ll m = d.size();
    vector<pair<ll, ll>> a;
    a.push_back(make_pair(0, 0));
    for (const auto &[k, p] : d) {
        a.push_back(make_pair(p.first, p.second));
    }
    a.push_back(make_pair(0, 0));

    vector<vector<ll>> dp(m + 2, vector<ll>(2, INF));
    dp[0][0] = 0;
    dp[0][1] = 0;
    // dp[i][j]:=i番目の色を使う時に右/左（j）にいる時のスコアの最小値

    rep(i, m + 1) {
        ll l, r, nl, nr;
        tie(l, r) = a[i];
        tie(nl, nr) = a[i + 1];
        rep(j, 2) {
            ll now_x = j ? r : l;
            chmin(dp[i + 1][0], dp[i][j] + abs(nr - now_x) + nr - nl);
            chmin(dp[i + 1][1], dp[i][j] + abs(nl - now_x) + nr - nl);
        }
        // if (l < nl) {
        //     chmin(dp[i + 1][1], dp[i][0] + nr - l);
        // } else if (nr < l) {
        //     chmin(dp[i + 1][0], dp[i][0] + l - nl);
        // } else {
        //     chmin(dp[i + 1][0], dp[i][0] + nr - nl + nr - l);
        //     chmin(dp[i + 1][1], dp[i][0] + nr - nl + l - nl);
        // }
        // if (r < nl) {
        //     chmin(dp[i + 1][1], dp[i][1] + nr - r);
        // } else if (nr < r) {
        //     chmin(dp[i + 1][0], dp[i][1] + r - nl);
        // } else {
        //     chmin(dp[i + 1][0], dp[i][1] + nr - nl + nr - r);
        //     chmin(dp[i + 1][1], dp[i][1] + nr - nl + r - nl);
        // }
    }

    cout << dp[m + 1][0] << "\n";
    // cout << min(dp[m + 1][0], dp[m + 1][1]) << "\n";
    return 0;
}