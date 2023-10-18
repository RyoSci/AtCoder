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
// #define max(x, y) ((x) > (y) ? (x) : (y))
// #define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#include <bits/stdc++.h>

// "https://algo-logic.info/tree-dp/"

/* Rerooting: 全方位木 DP
    問題ごとに以下を書き換える
    - 型DPと単位元
    - 型DPに対する二項演算 merge
    - まとめたDPを用いて新たな部分木のDPを計算する add_root
    計算量: O(N)
*/
struct DP {  // DP の型
    long long dp;
    DP(long long dp_) : dp(dp_) {}
};
struct Rerooting {
    /* start 問題ごとに書き換え */
    const DP identity =
        DP(0);  // 単位元(末端の値は add_root(identity) になるので注意)
    function<DP(DP, DP)> merge = [](DP dp_cum, DP d) -> DP {
        return DP(dp_cum.dp + d.dp);
    };
    function<DP(DP)> add_root = [](DP d) -> DP { return DP(d.dp); };
    /* end 問題ごとに書き換え */

    // グラフの定義
    struct Edge {
        int to;
    };
    using Graph = vector<vector<Edge>>;

    vector<vector<DP>>
        dp;  // dp[v][i]: vから出るi番目の有向辺に対応する部分木のDP
    vector<DP> ans;  // ans[v]: 頂点vを根とする木の答え
    Graph G;

    Rerooting(int N) : G(N) {
        dp.resize(N);
        ans.assign(N, identity);
    }

    void add_edge(int a, int b) { G[a].push_back({b}); }
    void build() {
        dfs(0);  // 普通に木DP
        // cout << "ans"
        //      << "\n";
        // rep(i, dp.size()) {
        //     for (auto a : dp[i]) cout << a.dp << " ";
        //     cout << endl;
        // }
        bfs(0, identity);  // 残りの部分木に対応するDPを計算
    }

    DP dfs(int v, int p = -1) {  // 頂点v, 親p
        DP dp_cum = identity;
        int deg = G[v].size();
        // dp[v] = vector<DP>(deg, identity);
        for (int i = 0; i < deg; i++) {
            int u = G[v][i].to;
            if (u == p) continue;
            dp[v][i].dp += dfs(u, v).dp;
            dp_cum = merge(dp_cum, dp[v][i]);
        }
        return add_root(dp_cum);
    }
    void bfs(int v, const DP& dp_p,
             int p = -1) {  // bfs だが、実装が楽なので中身は dfs になっている
        int deg = G[v].size();
        for (int i = 0; i < deg;
             i++) {  // 前のbfsで計算した有向辺に対応する部分木のDPを保存
            if (G[v][i].to == p) dp[v][i].dp += dp_p.dp;
        }
        vector<DP> dp_l(deg + 1, identity),
            dp_r(deg + 1, identity);  // 累積merge
        for (int i = 0; i < deg; i++) {
            dp_l[i + 1] = merge(dp_l[i], dp[v][i]);
        }
        for (int i = deg - 1; i >= 0; i--) {
            dp_r[i] = merge(dp_r[i + 1], dp[v][i]);
        }

        ans[v] = add_root(dp_l[deg]);  // 頂点 v の答え

        for (int i = 0; i < deg; i++) {  // 一つ隣の頂点に対しても同様に計算
            int u = G[v][i].to;
            if (u == p) continue;
            bfs(u, add_root(merge(dp_l[i], dp_r[i + 1])), v);
        }
    }
};

int main() {
    int N;
    cin >> N;
    Rerooting reroot(N);
    vector<ll> a(N - 1, 0), b(N - 1, 0);
    rep(i, N - 1) cin >> a[i] >> b[i];
    for (int i = 0; i < N - 1; i++) {
        a[i]--;
        b[i]--;
        reroot.add_edge(a[i], b[i]);
        reroot.add_edge(b[i], a[i]);
    }

    map<P, ll> d;
    ll q;
    cin >> q;
    rep(i, q) {
        ll t, e, x;
        cin >> t >> e >> x;
        e--;
        ll to, from;
        if (t == 1) {
            to = b[e];
            from = a[e];
            d[P(from, to)] += x;

        } else {
            to = a[e];
            from = b[e];
            d[P(from, to)] += x;
        }
    }

    // rep_e(e, d) {
    //     auto [key, val] = e;
    //     cout << key.first << ' ' << key.second << ' ' << val << "\n";
    // }
    rep(par, N) {
        ll deg = reroot.G[par].size();
        reroot.dp[par] = vector<DP>(deg, reroot.identity);
        ll j = 0;
        rep_e(to, reroot.G[par]) {
            ll chi = to.to;
            // cout << "par" << ' ' << par << ' ' << "chi" << ' ' << chi <<
            // "\n";
            if (d.count(P(par, chi)) > 0) {
                reroot.dp[par][j].dp += d[P(par, chi)];
            }
            j++;
        }
    }
    // rep(i, N) {
    //     for (auto a : reroot.dp[i]) cout << a.dp << " ";
    //     cout << endl;
    // }
    reroot.build();

    for (int i = 0; i < N; i++) {
        cout << reroot.ans[i].dp << endl;
    }
}