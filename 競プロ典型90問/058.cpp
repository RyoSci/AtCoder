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

int main() {
    ll n, k;
    cin >> n >> k;
    vector<vector<ll>> dp(61, vector<ll>(1e5));
    rep(i, 1e5) {
        ll tmp = i;
        ll res = 0;
        while (tmp > 0) {
            res += tmp % 10;
            tmp /= 10;
        }

        dp[0][i] = (i + res) % 100000;
    }

    rep(i, 60) {
        rep(j, 1e5) { dp[i + 1][j] = dp[i][dp[i][j]]; }
    }
    ll now = n;
    rep(i, 61) {
        if (k >> i & 1) {
            now = dp[i][now];
        }
        // cout << now << "\n";
    }
    cout << now << "\n";

    // rep(i, 4) {
    //     rep(j, 10) { cout << dp[i][j] << " "; }
    //     cout << endl;
    // }
    return 0;
}