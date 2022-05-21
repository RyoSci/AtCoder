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
    ll rs, cs;
    cin >> rs >> cs;
    ll rt, ct;
    cin >> rt >> ct;
    rs--, cs--;
    rt--, ct--;

    vector<vector<char>> s(h, vector<char>(w));
    rep(i, h) rep(j, w) cin >> s[i][j];
    vector<vector<vector<ll>>> cnt(4,
                                   vector<vector<ll>>(h, vector<ll>(w, INF)));

    // queue<T> q;
    deque<T> q;
    rep(i, 4) {
        cnt[i][rs][cs] = 0;
        q.emplace_back(make_tuple(i, rs, cs));
    }
    vector<ll> dr = {-1, 0, 1, 0};
    vector<ll> dc = {0, 1, 0, -1};

    while (!q.empty()) {
        auto [dir, r, c] = q.front();
        q.pop_front();
        ll nr, nc;
        rep(ndir, 4) {
            nr = r + dr[ndir];
            nc = c + dc[ndir];
            if (ndir == dir && 0 <= nr && nr < h && 0 <= nc && nc < w &&
                s[nr][nc] == '.') {
                if (cnt[ndir][nr][nc] > cnt[dir][r][c]) {
                    cnt[ndir][nr][nc] = cnt[dir][r][c];
                    q.emplace_front(make_tuple(ndir, nr, nc));
                }
            } else if (ndir != dir && 0 <= nr && nr < h && 0 <= nc && nc < w &&
                       s[nr][nc] == '.') {
                if (cnt[ndir][nr][nc] > cnt[dir][r][c] + 1) {
                    cnt[ndir][nr][nc] = cnt[dir][r][c] + 1;
                    q.emplace_back(make_tuple(ndir, nr, nc));
                }
            }
        }
    }

    ll ans = INF;
    rep(i, 4) ans = min(ans, cnt[i][rt][ct]);
    cout << ans << "\n";
    return 0;
}