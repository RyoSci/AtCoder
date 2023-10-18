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
// using mint = modint1000000007;
using mint = modint998244353;
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
    string s;
    cin >> s;
    vector<vector<ll>> dp(1 << 10, vector<ll>(10, 0));

    dp[0][0] = 1;
    rep(i, n) {
        ll now = s[i] - 'A';
        rep_r(j, (1 << 10) - 1, -1) {
            rep(k, 10) {
                // if (!(j & (1 << now))) continue;
                if ((j & (1 << now)) and now != k) continue;
                dp[j | (1 << now)][now] += dp[j][k];
                dp[j | (1 << now)][now] %= MOD;
            }
        }
    }

    mint ans = 0;
    rep_s(i, 1, 1 << 10) rep(j, 10) ans += dp[i][j];

    cout << ans.val() << "\n";
    return 0;
}