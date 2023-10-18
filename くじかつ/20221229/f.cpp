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
    ll sx, sy;
    cin >> sx >> sy;
    sx--;
    sy--;
    ll gx, gy;
    cin >> gx >> gy;
    gx--;
    gy--;

    vector<ll> x(n, 0), y(n, 0);
    rep(i, n) {
        cin >> x[i] >> y[i];
        x[i]--;
        y[i]--;
    }

    map<ll, vector<ll>> tate, yoko;
    rep(i, n) {
        tate[y[i]].emplace_back(x[i]);
        yoko[x[i]].emplace_back(y[i]);
    }
    rep(i, n) {
        sort(tate[y[i]].begin(), tate[y[i]].end());
        sort(yoko[x[i]].begin(), yoko[x[i]].end());
    }

    map<P, ll> dp;
    dp[P(sx, sy)] = 0;
    queue<P> q;
    q.emplace(P(sx, sy));

    auto check = [&](ll nx, ll ny, ll px, ll py) {
        if (dp.count(P(nx, ny)) == 0) {
            dp[P(nx, ny)] = dp[P(px, py)] + 1;
            q.emplace(P(nx, ny));
        }
    };

    while (q.size()) {
        auto [px, py] = q.front();
        q.pop();

        ll dis, nx, ny;
        if (tate[py].size() > 0) {
            dis = lower_bound(tate[py].begin(), tate[py].end(), px) -
                  tate[py].begin();
            ny = py;
            // 上
            if (dis != 0) {
                nx = tate[py][dis - 1] + 1;
                check(nx, ny, px, py);
            }
            // 下
            if (dis != tate[py].size()) {
                nx = tate[py][dis] - 1;
                check(nx, ny, px, py);
            }
        }
        if (yoko[px].size() > 0) {
            dis = lower_bound(yoko[px].begin(), yoko[px].end(), py) -
                  yoko[px].begin();
            nx = px;
            // 左
            if (dis != 0) {
                ny = yoko[px][dis - 1] + 1;
                check(nx, ny, px, py);
            }
            // 右
            if (dis != yoko[px].size()) {
                ny = yoko[px][dis] - 1;
                check(nx, ny, px, py);
            }
        }
    }

    if (dp[P(gx, gy)] == 0)
        cout << -1 << "\n";
    else
        cout << dp[P(gx, gy)] << "\n";

    return 0;
}