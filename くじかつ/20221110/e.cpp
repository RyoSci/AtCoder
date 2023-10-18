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
    ll n;
    cin >> n;
    map<ll, vector<ll>> d;
    rep(i, n) {
        ll x, c;
        cin >> x >> c;
        d[c].emplace_back(x);
    }

    d[INF].emplace_back(0);

    map<ll, ll> dp;
    dp[0] = 0;
    rep_e(e, d) {
        auto [c, ids] = e;
        sort(ids.begin(), ids.end());
        map<ll, ll> nxt;
        nxt[ids[0]] = INF;
        nxt[ids.back()] = INF;

        rep_e(f, dp) {
            auto [i, j] = f;
            chmin(nxt[ids.back()],
                  j + abs(ids[0] - i) + abs(ids.back() - ids[0]));
            chmin(nxt[ids[0]],
                  j + abs(ids.back() - i) + abs(ids[0] - ids.back()));
        }
        swap(dp, nxt);
    }

    ll ans = INF;
    rep_e(e, dp) {
        auto [key, val] = e;
        ans = min(ans, val);
    }
    cout << ans << "\n";
    return 0;
}