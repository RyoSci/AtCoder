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

vector<ll> par(2000 * 2000 + 10, -1);

ll root(ll x) {
    if (par[x] < 0) return x;
    return par[x] = root(par[x]);
}

bool same(ll x, ll y) { return root(x) == root(y); }

void unite(ll x, ll y) {
    x = root(x);
    y = root(y);
    if (x == y) return;
    if (par[x] > par[y]) swap(x, y);
    par[x] += par[y];
    par[y] = x;
    return;
}

int main() {
    ll h, w;
    cin >> h >> w;

    vector<ll> dx = {-1, 0, 1, 0};
    vector<ll> dy = {0, 1, 0, -1};

    vector<vector<ll>> grid(h, vector<ll>(w, 0));

    ll q;
    cin >> q;
    rep(i, q) {
        ll qi;
        cin >> qi;
        if (qi == 1) {
            ll r, c;
            cin >> r >> c;
            r--;
            c--;
            grid[r][c] = 1;
            rep(j, 4) {
                ll nr = r + dx[j];
                ll nc = c + dy[j];
                if (0 <= nr and nr < h and 0 <= nc and nc < w and
                    grid[nr][nc] == 1) {
                    unite(r * w + c, nr * w + nc);
                }
            }
        } else {
            ll ra, ca, rb, cb;
            cin >> ra >> ca >> rb >> cb;
            ra--;
            ca--;
            rb--;
            cb--;
            if (grid[ra][ca] and grid[rb][cb] and
                same(ra * w + ca, rb * w + cb))
                cout << "Yes"
                     << "\n";
            else
                cout << "No"
                     << "\n";
        }
    }

    return 0;
}