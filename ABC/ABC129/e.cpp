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
    string l;
    cin >> l;

    ll n = l.length();
    vector dp(n + 1, vector(3, vector(2, mint(0))));
    dp[0][0][0] = 1;

    rep(i, n) {
        rep(j, 3) {
            rep(nj, 3) { dp[i + 1][nj][1] += dp[i][j][1]; }
            if (l[i] == '1') {
                dp[i + 1][0][1] += dp[i][j][0];

                dp[i + 1][1][0] += dp[i][j][0];
                dp[i + 1][2][0] += dp[i][j][0];
            } else {
                dp[i + 1][0][0] += dp[i][j][0];
            }
        }
    }

    mint ans = 0;
    rep(j, 3) rep(k, 2) ans += dp[n][j][k];
    cout << ans.val() << "\n";

    return 0;
}