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
    vector<string> a(h);

    rep(i, h) { cin >> a[i]; }

    P s, g;
    vector<vector<P>> pos(26);

    rep(i, h) rep(j, w) {
        if (a[i][j] == 'S')
            s = P(i, j);
        else if (a[i][j] == 'G')
            g = P(i, j);
        else if (a[i][j] == '.' or a[i][j] == '#')
            continue;
        else {
            pos[a[i][j] - 'a'].emplace_back(P(i, j));
        }
    }

    vector<bool> seen(26, false);

    vector<ll> dx = {-1, 0, 1, 0};
    vector<ll> dy = {0, 1, 0, -1};

    queue<P> q;
    q.push(s);

    vector<vector<ll>> dis(h, vector<ll>(w, INF));
    dis[s.first][s.second] = 0;
    while (q.size() > 0) {
        auto [i, j] = q.front();
        q.pop();
        char c = a[i][j];
        if (c != '.' and c != 'S' and c != 'G') {
            if (!seen[c - 'a']) {
                seen[c - 'a'] = true;
                for (auto [ni, nj] : pos[c - 'a']) {
                    if (dis[ni][nj] > dis[i][j] + 1) {
                        dis[ni][nj] = dis[i][j] + 1;
                        q.push(P(ni, nj));
                    }
                }
            }
        }
        rep(k, 4) {
            ll ni = i + dx[k];
            ll nj = j + dy[k];
            if (0 <= ni and ni < h and 0 <= nj and nj < w and
                a[ni][nj] != '#' and dis[ni][nj] > dis[i][j] + 1) {
                dis[ni][nj] = dis[i][j] + 1;
                q.push(P(ni, nj));
            }
        }
    }

    if (dis[g.first][g.second] == INF)
        cout << -1 << "\n";
    else
        cout << dis[g.first][g.second] << "\n";

    return 0;
}