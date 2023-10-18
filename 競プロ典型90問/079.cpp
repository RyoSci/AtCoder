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

int main() {
    ll h, w;
    cin >> h >> w;
    vector<vector<ll>> a(h, vector<ll>(w, 0));
    rep(i, h) rep(j, w) cin >> a[i][j];
    vector<vector<ll>> b(h, vector<ll>(w, 0));
    rep(i, h) rep(j, w) cin >> b[i][j];

    ll ans = 0;
    rep(i, h - 1) rep(j, w - 1) {
        ll dis = b[i][j] - a[i][j];
        if (dis == 0) continue;
        ans += abs(dis);
        rep(ii, 2) rep(jj, 2) a[i + ii][j + jj] += dis;
    }
    if (a == b) {
        cout << "Yes"
             << "\n";
        cout << ans << "\n";
    } else
        cout << "No"
             << "\n";
    return 0;
}