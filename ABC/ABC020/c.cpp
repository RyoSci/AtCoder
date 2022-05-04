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

ll h, w, t;
vector<vector<char>> s(10, vector<char>(10));

ll sx, sy, gx, gy;

vector<ll> dx = {-1, 0, 1, 0};
vector<ll> dy = {0, 1, 0, -1};

ll bfs(ll mid) {
    queue<P> q;
    q.push(make_pair(sx, sy));
    vector<vector<ll>> dis(h, vector<ll>(w, INF));
    dis[sx][sy] = 0;
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        rep(i, 4) {
            ll nx = x + dx[i], ny = y + dy[i];
            if (0 <= nx && nx < h && 0 <= ny && 0 < w) {
                if (s[nx][ny] == '.' or s[nx][ny] == 'G') {
                    if (dis[nx][ny] > dis[x][y] + 1) {
                        dis[nx][ny] = dis[x][y] + 1;
                        q.push(make_pair(nx, ny));
                    }
                } else if (s[nx][ny] == '#') {
                    if (dis[nx][ny] > dis[x][y] + mid) {
                        dis[nx][ny] = dis[x][y] + mid;
                        q.push(make_pair(nx, ny));
                    }
                }
            }
        }
    }
    return dis[gx][gy];
}

int main() {
    cin >> h >> w >> t;
    rep(i, h) rep(j, w) cin >> s[i][j];
    rep(i, h) rep(j, w) {
        if (s[i][j] == 'S') sx = i, sy = j;
        if (s[i][j] == 'G') gx = i, gy = j;
    }

    ll ok = 1;
    ll ng = INF;
    while (ok + 1 < ng) {
        ll mid = (ok + ng) / 2;
        if (bfs(mid) <= t)
            ok = mid;
        else
            ng = mid;
    }
    cout << ok << "\n";
    return 0;
}