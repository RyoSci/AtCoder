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
    ll n, k;
    cin >> n >> k;
    vector<ll> costs(n);
    vector<ll> rests(n);
    rep(i, n) { cin >> costs[i] >> rests[i]; }

    vector<vector<ll>> g(n);
    rep(i, k) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    priority_queue<P> q;
    vector<ll> dis(n, INF);
    dis[0] = 0;
    q.push(make_pair(-dis[0], 0));
    while (!q.empty()) {
        ll d, par;
        tie(d, par) = q.top();
        q.pop();
        d = -d;

        if (dis[par] < d) continue;
        // 残っている乗車街分幅優先探索
        queue<P> qq;
        qq.push(make_pair(par, rests[par]));

        // 一度見たところを見てしまっていたので追記
        vector<bool> seen(n, 0);
        seen[par] = 1;

        while (!qq.empty()) {
            ll parpar, rest;
            tie(parpar, rest) = qq.front();
            qq.pop();
            if (rest == 0) continue;
            rep_e(chi, g[parpar]) {
                if (seen[chi]) continue;
                seen[chi] = 1;
                // 後々に更新できる場合があるので、行けるところまで行く。
                // 最小コストになっていない場合はダイクストラのqueueには突っ込まない。
                qq.push(make_pair(chi, rest - 1));
                // コストを足すのは大元の親から
                if (dis[chi] > dis[par] + costs[par]) {
                    dis[chi] = dis[par] + costs[par];
                    q.push(make_pair(-dis[chi], chi));
                }
            }
        }
    }
    cout << dis[n - 1] << "\n";
    // for (auto a : dis) cout << a << " ";
    // cout << endl;
    return 0;
}