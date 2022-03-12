// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll h, w;
    cin >> h >> w;
    vector<vector<char>> a(h, vector<char>(w));
    vector<vector<ll>> warp(26);

    ll si, sj, gi, gj;
    rep(i, h) {
        rep(j, w) {
            cin >> a[i][j];
            ll tmp = a[i][j] - 'a';
            if (0 <= tmp && tmp < 26) {
                warp[tmp].push_back(i * 4000 + j);
            } else if (a[i][j] == 'S') {
                si = i;
                sj = j;
            } else if (a[i][j] == 'G') {
                gi = i;
                gj = j;
            }
        }
    }

    queue<P> q;
    q.push(make_pair(si, sj));
    vector<vector<ll>> dis(h, vector<ll>(w, INF));
    dis[si][sj] = 0;

    vector<ll> di{-1, 0, 1, 0};
    vector<ll> dj{0, 1, 0, -1};

    vector<ll> seen(26, 0);

    while (!q.empty()) {
        auto par = q.front();
        q.pop();
        ll i, j;
        i = par.first;
        j = par.second;

        ll ni, nj;
        // 上下左右
        rep(k, 4) {
            ni = i + di[k];
            nj = j + dj[k];
            if (0 <= ni && ni < h && 0 <= nj && nj < w && a[ni][nj] != '#') {
                if (dis[ni][nj] > dis[i][j] + 1) {
                    dis[ni][nj] = dis[i][j] + 1;
                    q.push(make_pair(ni, nj));
                }
            }
        }
        ll tmp = a[i][j] - 'a';
        // もしアルファベットだった場合
        if (0 <= tmp && tmp < 26 && !seen[tmp]) {
            rep_e(chi, warp[tmp]) {
                ni = chi / 4000;
                nj = chi % 4000;
                if (ni == i && nj == j) continue;
                if (dis[ni][nj] > dis[i][j] + 1) {
                    dis[ni][nj] = dis[i][j] + 1;
                    q.push(make_pair(ni, nj));
                }
            }
            seen[tmp] = 1;
        }
    }

    if (dis[gi][gj] == INF)
        cout << -1 << "\n";
    else
        cout << dis[gi][gj] << "\n";
    return 0;
}