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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        string s;
        cin >> s;

        vector dp(n + 1, vector(2, mint(0)));
        dp[0][0] = 1;

        rep(i, (n + 1) / 2) {
            dp[i + 1][0] += dp[i][0];
            dp[i + 1][1] += dp[i][0] * (s[i] - 'A');
            dp[i + 1][1] += dp[i][1] * 26;
        }
        rep_s(i, (n + 1) / 2, n) {
            if (s[n - 1 - i] == s[i])
                dp[i + 1][0] += dp[i][0];
            else if (s[n - 1 - i] < s[i])
                dp[i + 1][1] += dp[i][0];

            dp[i + 1][1] += dp[i][1];
        }
        cout << (dp[n][0] + dp[n][1]).val() << "\n";
    }
    return 0;
}