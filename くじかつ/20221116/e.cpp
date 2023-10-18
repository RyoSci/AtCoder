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

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> b(n);
    for (ll i = 0; i < n; i++) cin >> b[i];

    vector<P> ab(n);
    rep(i, n) { ab[i] = P(a[i], b[i]); }

    sort(ab.begin(), ab.end());

    vector<vector<mint>> dp(n + 1, vector<mint>(5010, 0));
    dp[0][0] = 1;

    rep(i, n) {
        auto [ai, bi] = ab[i];
        rep(j, 5010) {
            dp[i + 1][j] += dp[i][j];
            if (j + bi > 5000) continue;
            dp[i + 1][j + bi] += dp[i][j];
        }
    }

    mint ans = 0;
    rep(i, n) {
        auto [ai, bi] = ab[i];
        ll rest = ai - bi;
        rep_s(j, 0, rest + 1) { ans += dp[i][j]; }
    }
    cout << ans.val() << "\n";
    // rep(i, n + 1) {
    //     for (auto a : dp[i]) cout << a.val() << " ";
    //     cout << endl;
    // }
    return 0;
}