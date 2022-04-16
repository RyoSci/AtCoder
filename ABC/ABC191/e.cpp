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
    ll n, m;
    cin >> n >> m;
    vector<ll> a(m), b(m), c(m);
    for (ll i = 0; i < m; i++) cin >> a[i] >> b[i] >> c[i];
    vector<vector<P>> g(n);
    vector<ll> ans(n, INF);

    rep(i, m) {
        a[i]--;
        b[i]--;
        g[a[i]].push_back(make_pair(b[i], c[i]));
        if (a[i] == b[i]) ans[a[i]] = min(ans[a[i]], c[i]);
    }

    // iからスタートして各頂点の距離の最小値
    vector<vector<ll>> dis(n, vector<ll>(n, INF));

    rep(i, n) {
        priority_queue<P> q;
        dis[i][i] = 0;
        q.push(make_pair(-dis[i][i], i));
        while (!q.empty()) {
            ll d, par;
            tie(d, par) = q.top();
            q.pop();
            d = -d;
            if (d > dis[i][par]) continue;
            rep_e(e, g[par]) {
                ll chi, dd;
                tie(chi, dd) = e;
                if (dis[i][chi] > dis[i][par] + dd) {
                    dis[i][chi] = dis[i][par] + dd;
                    q.push(make_pair(-dis[i][chi], chi));
                }
            }
        }
    }

    rep(i, n) {
        rep(j, n) {
            if (i == j) continue;
            if (dis[i][j] != INF && dis[j][i] != INF)
                ans[i] = min(ans[i], dis[i][j] + dis[j][i]);
        }
        if (ans[i] != INF)
            cout << ans[i] << "\n";
        else
            cout << -1 << "\n";
    }

    return 0;
}