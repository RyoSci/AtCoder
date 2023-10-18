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
    vector<ll> a(m), b(m);
    for (ll i = 0; i < m; i++) cin >> a[i] >> b[i];

    vector<ll> p(n, 0);
    vector<vector<ll>> g(n);

    rep(i, m) {
        g[a[i] - 1].push_back(b[i] - 1);
        p[b[i] - 1]++;
    }

    priority_queue<ll> q;
    rep(i, n) {
        if (p[i] == 0) q.emplace(-i);
    }

    vector<ll> ans;
    while (!q.empty()) {
        ll to = q.top();
        to = -to;
        ans.emplace_back(to + 1);
        q.pop();
        rep_e(e, g[to]) {
            p[e]--;
            if (p[e] == 0) q.emplace(-e);
        }
    }

    if (ans.size() == n) {
        for (auto a : ans) cout << a << " ";
        cout << endl;
    } else {
        cout << -1 << "\n";
    }

    return 0;
}