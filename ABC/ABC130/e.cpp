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
using mint = modint1000000007;
// using mint = modint998244353;
// #define MOD 1000000007
#define MOD 998244353
#define INF (1LL << 60)
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
    ll n, m;
    cin >> n >> m;
    vector<ll> s(n);
    for (ll i = 0; i < n; i++) cin >> s[i];
    vector<ll> t(m);
    for (ll i = 0; i < m; i++) cin >> t[i];

    vector dp(n + 1, vector(m + 1, mint(0)));

    dp[0][0] = 1;
    mint ans = 1;
    rep(i, n) {
        mint cnt = 0;
        rep(j, m + 1) {
            cnt += dp[i][j];
            if (j < m and s[i] == t[j]) {
                dp[i + 1][j + 1] += cnt;
                ans += cnt;
            }
            dp[i + 1][j] += dp[i][j];
        }
    }

    cout << ans.val() << "\n";
    return 0;
}