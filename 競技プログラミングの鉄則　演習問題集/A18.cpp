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
    ll n, s;
    cin >> n >> s;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    vector dp(n + 1, vector(s + 1, 0ll));

    dp[0][0] = 1;

    rep(i, n) {
        rep(j, s + 1) {
            if (dp[i][j] == 0) continue;
            dp[i + 1][j] = dp[i][j];
            if (j + a[i] <= s) dp[i + 1][j + a[i]] = dp[i][j];
        }
    }

    cout << (dp[n][s] ? "Yes" : "No") << "\n";
    return 0;
}