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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n, m;
        cin >> n >> m;
        vector<ll> a(n + 1);
        for (ll i = 0; i < n; i++) cin >> a[i + 1];
        a[0] = m;
        vector<ll> dp(n + 1, 0);
        dp[0] = m;
        bool ans = true;
        rep(i, n) {
            // if (dp[i] != a[i]) ans = false;
            // ll use = min(a[i + 1] - dp[i + 1], dp[i]);
            // if (use < 0) ans = false;
            // dp[i + 1] += use;
            // dp[min(n, i + 2)] += dp[i] - use;
            if (a[i + 1] - dp[i + 1] > dp[i] or a[i + 1] < dp[i + 1]) {
                ans = false;
                break;
            } else {
                ll use = a[i + 1] - dp[i + 1];
                dp[i + 1] += use;
                dp[min(n - 1, i + 2)] += dp[i] - use;
            }
        }
        cout << (ans ? "Yes" : "No") << "\n";
    }
    return 0;
}