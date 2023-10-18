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
    for (ll i = 0; i < n; i++) cin >> a[i];
    ll ans = INF;
    rep(i, 1 << (n - 1)) {
        vector<ll> tot;
        ll now = a[0];
        rep(j, n - 1) {
            if (i >> j & 1) {
                tot.emplace_back(now);
                now = a[j + 1];
            } else {
                now |= a[j + 1];
            }
        }
        tot.emplace_back(now);

        ll res = 0;
        rep(j, tot.size()) res ^= tot[j];

        ans = min(ans, res);
    }

    cout << ans << "\n";
    return 0;
}