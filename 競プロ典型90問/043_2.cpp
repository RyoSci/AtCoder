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

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll h, w;
    cin >> h >> w;
    ll rs, cs, rt, ct;
    cin >> rs >> cs >> rt >> ct;
    rs--;
    cs--;
    rt--;
    ct--;
    vector<string> s(h);
    rep(i, h) cin >> s[i];

    vector<vector<vector<ll>>> dis(h,
                                   vector<vector<ll>>(w, vector<ll>(4, INF)));

    rep(i, 4) dis[rs][cs][i] = 0;
    queue<T> q;
    // x,y,dir
    rep(i, 4) q.emplace(T{rs, cs, i});

    vector<ll> dx = {-1, 0, 1, 0};
    vector<ll> dy = {0, 1, 0, -1};

    while (q.size() > 0) {
        auto [x, y, dir] = q.front();
        q.pop();
        rep(i, 4) {
            ll nx, ny;
            nx = x + dx[i];
            ny = y + dy[i];
            if (!(0 <= nx and nx < h and 0 <= ny and ny < w and
                  s[nx][ny] == '.'))
                continue;
            if (dir == i) {
                if (dis[nx][ny][i] > dis[x][y][dir]) {
                    dis[nx][ny][i] = dis[x][y][dir];
                    q.emplace(T{nx, ny, i});
                }
            } else {
                if (dis[nx][ny][i] > dis[x][y][dir] + 1) {
                    dis[nx][ny][i] = dis[x][y][dir] + 1;
                    q.emplace(T{nx, ny, i});
                }
            }
        }
    }
    ll ans = INF;
    rep(i, 4) chmin(ans, dis[rt][ct][i]);
    cout << ans << "\n";
    return 0;
}