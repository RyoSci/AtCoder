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
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 1; i < n; i++) cin >> a[i];
    vector<ll> b(n);
    for (ll i = 2; i < n; i++) cin >> b[i];

    auto chmin = [&](ll& x, ll y) {
        if (x > y) x = y;
        return;
    };

    vector<ll> dp(n + 1, INF);
    dp[1] = 0;
    rep(i, n) {
        if (dp[i] == INF) continue;
        if (i + 1 <= n) chmin(dp[i + 1], dp[i] + a[i + 1 - 1]);
        if (i + 2 <= n) chmin(dp[i + 2], dp[i] + b[i + 2 - 1]);
    }

    cout << dp[n] << "\n";
    return 0;
}