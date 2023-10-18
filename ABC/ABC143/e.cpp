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
    ll n, m, l;
    cin >> n >> m >> l;
    vector<vector<P>> g(n);
    rep(i, m) {
        ll a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        g[a].emplace_back(b, c);
        g[b].emplace_back(a, c);
    }

    vector dp(n, vector(n, INF));
    vector oil(n, vector(n, -1));
    rep(i, n) {
        dp[i][i] = 0;
        oil[i][i] = l;
        priority_queue<T> pq;
        pq.emplace(-dp[i][i], oil[i][i], i);
        while (pq.size()) {
            auto [cnt, rest, par] = pq.top();
            pq.pop();
            cnt *= -1;
            if (dp[i][par] != cnt or oil[i][par] != rest) continue;
            for (auto [chi, c] : g[par]) {
                if (c <= rest) {
                    if (dp[i][chi] > dp[i][par]) {
                        dp[i][chi] = dp[i][par];
                        oil[i][chi] = oil[i][par] - c;
                        pq.emplace(-dp[i][chi], oil[i][chi], chi);
                    } else if (dp[i][chi] == dp[i][par] and
                               oil[i][chi] < oil[i][par] - c) {
                        oil[i][chi] = oil[i][par] - c;
                        pq.emplace(-dp[i][chi], oil[i][chi], chi);
                    }
                } else if (c <= l) {
                    if (dp[i][chi] > dp[i][par] + 1) {
                        dp[i][chi] = dp[i][par] + 1;
                        oil[i][chi] = l - c;
                        pq.emplace(-dp[i][chi], oil[i][chi], chi);
                    } else if (dp[i][chi] == dp[i][par] + 1 and
                               oil[i][chi] < l - c) {
                        oil[i][chi] = l - c;
                        pq.emplace(-dp[i][chi], oil[i][chi], chi);
                    }
                }
            }
        }
    }

    ll q;
    cin >> q;
    rep(i, q) {
        ll s, t;
        cin >> s >> t;
        s--;
        t--;
        if (dp[s][t] == INF)
            cout << -1 << "\n";
        else
            cout << dp[s][t] << "\n";
    }
    return 0;
}