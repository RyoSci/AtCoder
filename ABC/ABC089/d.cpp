// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll h, w, d;
    cin >> h >> w >> d;
    vector<vector<ll>> a(h, vector<ll>(w, 0));
    rep(i, h) rep(j, w) { cin >> a[i][j]; }
    vector<P> pos(h * w + 1);

    rep(i, h) rep(j, w) { pos[a[i][j]] = make_pair(i, j); }
    vector<ll> dis(h * w + 1, 0);
    rep(i, d) {
        ll pre = h * w - i;
        while (pre - d > 0) {
            ll px, py;
            tie(px, py) = pos[pre];
            ll now = pre - d;
            ll nx, ny;
            tie(nx, ny) = pos[now];
            dis[now] = dis[pre] + abs(px - nx) + abs(py - ny);
            pre = now;
        }
    }

    ll q;
    cin >> q;
    rep(i, q) {
        ll l, r;
        cin >> l >> r;
        cout << dis[l] - dis[r] << "\n";
    }

    return 0;
}