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
    ll n, m, x;
    cin >> n >> m >> x;
    vector<ll> c(n, 0);
    vector a(n, vector(m, 0ll));
    rep(i, n) {
        cin >> c[i];
        rep(j, m) cin >> a[i][j];
    }

    ll ans = INF;
    rep(i, 1 << n) {
        vector<ll> skills(m, 0);
        ll cost = 0;
        rep(j, n) {
            if (i >> j & 1) {
                cost += c[j];
                rep(k, m) skills[k] += a[j][k];
            }
        }

        bool flag = true;
        rep(j, m) if (skills[j] < x) flag = false;
        if (flag) ans = min(ans, cost);
    }
    if (ans == INF)
        cout << -1 << "\n";
    else
        cout << ans << "\n";
    return 0;
}