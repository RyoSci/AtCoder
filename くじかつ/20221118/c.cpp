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

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    set<ll> ele;
    rep(i, n) {
        ll now = a[i];
        for (ll j = 2; j * j <= a[i]; j++) {
            while (now % j == 0) {
                ele.insert(j);
                now /= j;
            }
        }
        if (now > 1) ele.insert(now);
    }

    vector<bool> ok(m + 1, 1);
    ok[0] = 0;
    rep_e(e, ele) {
        if (e > m) continue;
        if (ok[e] == 0) continue;
        for (ll i = e; i <= m; i += e) {
            ok[i] = 0;
        }
    }

    ll cnt = 0;
    rep(i, m + 1) if (ok[i]) cnt++;
    cout << cnt << "\n";
    rep(i, m + 1) if (ok[i]) cout << i << "\n";
    return 0;
}