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
    ll h, w, n;
    cin >> h >> w >> n;
    vector g(h + 1, vector(w + 1, 0ll));
    rep(i, n) {
        ll a, b, c, d;
        cin >> a >> b >> c >> d;
        a--;
        b--;
        c--;
        d--;
        g[a][b]++;
        g[a][d + 1]--;
        g[c + 1][b]--;
        g[c + 1][d + 1]++;
    }

    rep(i, h) rep(j, w) g[i][j + 1] += g[i][j];
    rep(j, w) rep(i, h) g[i + 1][j] += g[i][j];

    rep(i, h) {
        rep(j, w) cout << g[i][j] << " ";
        cout << "\n";
    }
    return 0;
}