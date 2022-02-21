#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
#include <bits/stdc++.h>

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
    ll v, e, r;
    cin >> v >> e >> r;
    vector<vector<P>> g(v);
    rep(i, e) {
        ll s, t, d;
        cin >> s >> t >> d;
        g[s].push_back(make_pair(t, d));
    }

    vector<ll> dis(v, INF);
    dis[r] = 0;
    priority_queue<P> q;
    q.push(make_pair(-dis[r], r));

    while (!q.empty()) {
        ll d = -q.top().first;
        ll now = q.top().second;
        q.pop();

        // nowまでの距離現在の最小値より大きい場合はゴミ
        if (dis[now] < d) continue;
        rep_e(chi, g[now]) {
            ll to = chi.first;
            ll d_from_now = chi.second;
            if (d + d_from_now < dis[to]) {
                dis[to] = d + d_from_now;
                q.push(make_pair(-dis[to], to));
            }
        }
    }

    rep(i, v) {
        if (dis[i] == INF)
            cout << "INF"
                 << "\n";
        else
            cout << dis[i] << "\n";
    }
    return 0;
}