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

ll h, w;

vector<ll> par;
vector<string> c;

ll root(ll x) {
    if (par[x] < 0) return x;
    return par[x] = root(par[x]);
}

bool same(ll x, ll y) { return root(x) == root(y); }

void unite(ll x, ll y) {
    ll px = root(x);
    ll py = root(y);
    if (px == py) return;
    if (px > py) swap(px, py);
    par[px] += par[py];
    par[py] = px;
    return;
}

vector<ll> di = {-1, 0, 1, 0};
vector<ll> dj = {0, 1, 0, -1};

void dfs(ll x, ll y, ll px, ll py) {
    rep(i, 4) {
        ll nx = x + di[i];
        ll ny = y + dj[i];
        if (nx == px and ny == py) continue;
        if (0 <= nx and nx < h and 0 <= ny and ny < w and c[nx][ny] == '.') {
            if (!same(x * w + y, nx * w + ny)) {
                unite(x * w + y, nx * w + ny);
                dfs(nx, ny, x, y);
            }
        }
    }
}

int main() {
    cin >> h >> w;
    c.resize(h);
    rep(i, h) cin >> c[i];

    par.resize(h * w, -1);

    ll si, sj;
    rep(i, h) rep(j, w) {
        if (c[i][j] == 'S') {
            si = i;
            sj = j;
        }
    }

    rep(num, 4) {
        ll ni = si + di[num];
        ll nj = sj + dj[num];
        if (0 <= ni and ni < h and 0 <= nj and nj < w and c[ni][nj] == '.') {
            dfs(ni, nj, -1, -1);
        }
    }

    bool ans = false;
    rep(i, 4) {
        ll ix = si + di[i];
        ll iy = sj + dj[i];
        if (0 <= ix and ix < h and 0 <= iy and iy < w and c[ix][iy] == '.') {
            rep(j, 4) {
                if (i == j) continue;
                ll jx = si + di[j];
                ll jy = sj + dj[j];
                if (0 <= jx and jx < h and 0 <= jy and jy < w and
                    c[jx][jy] == '.') {
                    if (same(ix * w + iy, jx * w + jy)) ans = true;
                    // if (root(ix * w + iy) == root(jx * w + jy)) ans = true;
                    // cout << i << ' ' << j << ' ' << ans << "\n";
                    // cout << root(ix * w + iy) << ' ' << root(jx * w + jy) <<
                    // ' '
                    //      << ans << "\n";
                }
            }
        }
    }
    cout << (ans ? "Yes" : "No") << "\n";
    // rep(i, h) {
    //     rep(j, w) { cout << par[i * w + j] << " "; }
    //     cout << "\n";
    // }

    return 0;
}