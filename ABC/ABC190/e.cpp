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
    ll n, m;
    cin >> n >> m;
    vector<vector<ll>> g(n);
    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].emplace_back(b);
        g[b].emplace_back(a);
    }

    ll k;
    cin >> k;
    vector<ll> c(k);
    set<ll> s;
    for (ll i = 0; i < k; i++) {
        cin >> c[i];
        c[i]--;
        s.insert(c[i]);
    }

    ll ans = 0;
    ll now = c[0];
    rep(i, k - 1) {
        vector<ll> dis(n, INF);
        dis[now] = 0;
        s.erase(now);

        queue<ll> q;
        q.emplace(now);
        ll res = INF;
        while (q.size() > 0) {
            ll par = q.front();
            q.pop();
            bool flag = false;
            rep_e(chi, g[par]) {
                if (dis[chi] > dis[par] + 1) {
                    dis[chi] = dis[par] + 1;
                    if (s.count(chi) > 0) {
                        res = dis[chi];
                        now = chi;
                        // cout << now << "\n";
                        flag = true;
                        break;
                    }
                    q.emplace(chi);
                }
            }
            if (flag) break;
        }

        if (res == INF) {
            cout << -1 << "\n";
            return 0;
        } else {
            ans += res;
            // cout << ans << "\n";
        }
    }
    cout << ans + 1 << "\n";
    return 0;
}