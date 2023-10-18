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
    ll n, m;
    cin >> n >> m;

    map<ll, vector<ll>> g;

    rep(i, m) {
        ll x, y;
        cin >> x >> y;
        g[y].emplace_back(x);
    }

    rep_e(e, g) {
        auto [key, vals] = e;
        sort(g[key].begin(), g[key].end());
    }

    ll x = 0;
    ll y = n;

    queue<P> q;
    q.emplace(x, y);
    set<P> seen;
    set<ll> ans;

    while (q.size()) {
        auto [x, y] = q.front();
        q.pop();

        // 真下
        auto iter = upper_bound(g[y].begin(), g[y].end(), x);
        ll nx;
        if (iter == g[y].end()) {
            ans.insert(y);
            nx = INF;
        } else {
            nx = *iter;
        }

        // 右隣
        if (y + 1 <= 2 * n) {
            iter = upper_bound(g[y + 1].begin(), g[y + 1].end(), x);
            ll rx;
            while (iter != g[y + 1].end()) {
                rx = *iter;
                if (rx <= nx and seen.count(P(rx, y + 1)) == 0) {
                    seen.insert(P(rx, y + 1));
                    q.emplace(rx, y + 1);
                }
                iter++;
            }
        }

        // 左隣
        if (y - 1 >= 0) {
            iter = upper_bound(g[y - 1].begin(), g[y - 1].end(), x);
            ll lx;
            while (iter != g[y - 1].end()) {
                lx = *iter;
                if (lx <= nx and seen.count(P(lx, y - 1)) == 0) {
                    seen.insert(P(lx, y - 1));
                    q.emplace(lx, y - 1);
                }
                iter++;
            }
        }
    }

    cout << ans.size() << "\n";

    return 0;
}