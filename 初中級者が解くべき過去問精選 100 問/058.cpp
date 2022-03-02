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

int main() {
    ll n, m, k, s;
    cin >> n >> m >> k >> s;
    ll p, q;
    cin >> p >> q;

    //    ゾンビの街なら-1, 近い街なら 0, 安全な街なら1
    vector<ll> safe(n, 1);
    rep(i, k) {
        ll id;
        cin >> id;
        id--;
        safe[id] = -1;
    }

    vector<vector<ll>> g(n);
    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    //    近い街を探索する
    queue<ll> que;
    vector<ll> dis(n, INF);
    rep(i, n) {
        if (safe[i] == -1) {
            que.push(i);
            dis[i] = 0;
        }
    }
    while (!que.empty()) {
        ll par = que.front();
        que.pop();
        rep_e(chi, g[par]) {
            if (dis[chi] > dis[par] + 1) {
                dis[chi] = dis[par] + 1;
                que.push(chi);
            }
        }
    }

    rep(i, n) {
        if (dis[i] <= s && safe[i] != -1) safe[i] = 0;
    }

    //    最短コストになるようにダイクストラ法で進んでいく
    priority_queue<pair<ll, ll>> heap;
    vector<ll> costs(n, INF);
    costs[0] = 0;
    heap.push(make_pair(-costs[0], 0));
    while (!heap.empty()) {
        ll d, par;
        tie(d, par) = heap.top();
        heap.pop();
        d = -d;
        // ゴミが出るので無視する。
        if (costs[par] < d) continue;
        rep_e(chi, g[par]) {
            ll dd;
            if (safe[chi] == -1)
                continue;
            else if (safe[chi] == 0)
                dd = costs[par] + q;
            else
                dd = costs[par] + p;

            if (costs[chi] > dd) {
                costs[chi] = dd;
                heap.push(make_pair(-costs[chi], chi));
            }
        }
    }
    cout << (safe[n - 1] ? costs[n - 1] - p : costs[n - 1] - q) << "\n";
    return 0;
}