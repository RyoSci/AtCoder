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
#define _GLIBCXX_DEBUG

ll n, k;
vector<vector<P>> g(1000);

ll dijkstra(ll a, ll b) {
    vector<ll> dis(n, INF);
    dis[a] = 0;
    priority_queue<P> q;
    q.push(make_pair(-dis[a], a));

    while (!q.empty()) {
        ll d, now;
        tie(d, now) = q.top();
        q.pop();
        d = -d;

        // ゴミの場合も紛れているのでスキップする
        if (dis[now] < d) continue;
        rep_e(node, g[now]) {
            ll chi, from_chi;
            tie(chi, from_chi) = node;
            if (dis[chi] > d + from_chi) {
                dis[chi] = d + from_chi;
                q.push(make_pair(-dis[chi], chi));
            }
        }
    }

    if (dis[b] == INF)
        return -1;
    else
        return dis[b];
}

int main() {
    cin >> n >> k;
    rep(i, k) {
        ll id;
        cin >> id;
        if (id == 0) {
            ll a, b;
            cin >> a >> b;
            a--;
            b--;
            ll ans = dijkstra(a, b);
            cout << ans << "\n";
        } else {
            ll c, d, e;
            cin >> c >> d >> e;
            c--;
            d--;
            g[c].push_back(make_pair(d, e));
            g[d].push_back(make_pair(c, e));
        }
    }
    return 0;
}