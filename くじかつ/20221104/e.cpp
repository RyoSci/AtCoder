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

void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> a(k);
    for (ll i = 0; i < k; i++) cin >> a[i];

    vector<ll> dp(n + 1, 0);
    dp[1] = 1;

    rep_s(i, 2, n + 1) {
        rep(j, k) {
            if (i - a[j] >= 0) chmax(dp[i], a[j] + i - a[j] - dp[i - a[j]]);
        }
    }

    cout << dp[n] << "\n";

    return 0;
}