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
    ll n, s;
    cin >> n >> s;
    vector<ll> a(n), b(n);
    for (ll i = 0; i < n; i++) cin >> a[i] >> b[i];

    vector<vector<ll>> dp(n + 1, vector<ll>(s + 1, 0));
    dp[0][0] = 1;

    vector<vector<P>> pre(n + 1, vector<P>(s + 1));

    rep(i, n) {
        rep(j, s + 1) {
            if (dp[i][j] == 0) continue;

            if (j + a[i] <= s) {
                dp[i + 1][j + a[i]] = dp[i][j];
                pre[i + 1][j + a[i]] = P{0, j};
            }
            if (j + b[i] <= s) {
                dp[i + 1][j + b[i]] = dp[i][j];
                pre[i + 1][j + b[i]] = P{1, j};
            }
        }
    }

    if (dp[n][s] == 0)
        cout << "Impossible"
             << "\n";
    else {
        string ans = "";
        ll pos = s;
        rep_r(i, n, 0) {
            auto [flag, nxt] = pre[i][pos];
            if (flag)
                ans += "B";
            else
                ans += "A";
            pos = nxt;
        }
        reverse(ans.begin(), ans.end());
        cout << ans << "\n";
    }
    return 0;
}