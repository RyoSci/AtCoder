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
    ll n, x, y;
    cin >> n >> x >> y;

    vector<vector<ll>> g(n);
    rep(i, n - 1) {
        g[i].emplace_back(i + 1);
        g[i + 1].emplace_back(i);
    }
    x--;
    y--;

    g[x].emplace_back(y);
    g[y].emplace_back(x);

    vector<ll> ans(n, 0);

    rep(i, n) {
        vector<ll> dis(n, INF);
        dis[i] = 0;
        queue<ll> q;
        q.emplace(i);
        while (q.size() > 0) {
            ll now = q.front();
            q.pop();
            rep_e(nxt, g[now]) {
                if (dis[nxt] > dis[now] + 1) {
                    dis[nxt] = dis[now] + 1;
                    q.emplace(nxt);
                }
            }
        }
        rep(i, n) { ans[dis[i]]++; }
    }
    rep_s(i, 1, n) cout << ans[i] / 2 << "\n";
    return 0;
}