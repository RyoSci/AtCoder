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
    ll h, w;
    cin >> h >> w;
    vector<string> g(h);
    rep(i, h) cin >> g[i];

    ll x = 0, y = 0;

    auto inner = [&](ll x, ll y) {
        return 0 <= x and x < h and 0 <= y and y < w;
    };

    set<P> s;
    while (1) {
        ll nx, ny;
        if (g[x][y] == 'U') nx = x - 1, ny = y;
        if (g[x][y] == 'D') nx = x + 1, ny = y;
        if (g[x][y] == 'L') nx = x, ny = y - 1;
        if (g[x][y] == 'R') nx = x, ny = y + 1;

        if (inner(nx, ny))
            x = nx, y = ny;
        else
            break;

        if (s.count(P(x, y)) > 0) {
            cout << -1 << "\n";
            return 0;
        }
        s.insert(P(x, y));
    }

    cout << x + 1 << ' ' << y + 1 << "\n";
    return 0;
}