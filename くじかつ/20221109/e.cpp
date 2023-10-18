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

ll pow_ll(ll n, ll p) {
    ll res = 1;
    while (p) {
        if (p % 2 == 1) res *= n;
        n *= n;
        p >>= 1;
    }
    return res;
}

void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> bit_counts(50, 0);
    rep(i, n) {
        rep(j, 50) {
            if (a[i] >> j & 1) bit_counts[j] += 1;
        }
    }

    vector<vector<ll>> dp(50, vector<ll>(2, -1));
    dp[0][1] = 0;

    rep(i, 49) {
        if ((k >> (48 - i)) & 1) {
            chmax(dp[i + 1][1],
                  dp[i][1] + pow_ll(2, 48 - i) * (n - bit_counts[48 - i]));
            chmax(dp[i + 1][0],
                  dp[i][1] + pow_ll(2, 48 - i) * (bit_counts[48 - i]));

        } else {
            chmax(dp[i + 1][1],
                  dp[i][1] + pow_ll(2, 48 - i) * (bit_counts[48 - i]));
        }
        if (dp[i][0] != -1) {
            chmax(dp[i + 1][0],
                  dp[i][0] + pow_ll(2, 48 - i) * max(n - bit_counts[48 - i],
                                                     bit_counts[48 - i]));
        }
    }

    cout << max(dp[49][0], dp[49][1]) << "\n";
    // rep(i, 50) {
    //     for (auto a : dp[i]) cout << a << " ";
    //     cout << endl;
    // }
    // for (auto a : bit_counts) cout << a << " ";
    // cout << endl;
    return 0;
}