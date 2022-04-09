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
    ll n;
    cin >> n;
    ll a, b;
    cin >> a >> b;
    a--;
    b--;
    ll m;
    cin >> m;
    vector<vector<ll>> g(n);

    rep(i, m) {
        ll x, y;
        cin >> x >> y;
        x--;
        y--;
        g[x].push_back(y);
        g[y].push_back(x);
    }

    vector<ll> dis(n, INF);
    vector<ll> cnt(n, 0);
    dis[a] = 0;
    cnt[a] = 1;
    queue<ll> q;
    q.push(a);
    while (!q.empty()) {
        ll par = q.front();
        q.pop();

        rep_e(chi, g[par]) {
            if (dis[chi] > dis[par] + 1) {
                dis[chi] = dis[par] + 1;
                q.push(chi);
                cnt[chi] += cnt[par];
                cnt[chi] %= MOD;
            } else if (dis[chi] == dis[par] + 1) {
                // dis[chi] = dis[par] + 1;
                // q.push(chi);
                cnt[chi] += cnt[par];
                cnt[chi] %= MOD;
            }
        }
    }

    cout << cnt[b] << "\n";

    return 0;
}