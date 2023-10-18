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

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> dp(1 << n, INF);

    dp[0] = 0;

    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        ll mask = 0;
        rep(j, b) {
            ll c;
            cin >> c;
            c--;
            mask |= (1 << c);
        }
        rep(k, 1 << n) { chmin(dp[k | mask], dp[k] + a); }
    }

    if (dp[(1 << n) - 1] == INF)
        cout << -1 << "\n";
    else
        cout << dp[(1 << n) - 1] << "\n";
    return 0;
}