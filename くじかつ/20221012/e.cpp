// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
// #include <priority_queue>
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
    vector<ll> a(n), b(n);
    for (ll i = 0; i < n; i++) cin >> a[i] >> b[i];

    priority_queue<ll> pq;
    vector<vector<ll>> d(m + 1);

    rep(i, n) {
        if (a[i] <= m) d[a[i]].emplace_back(b[i]);
    }

    ll ans = 0;
    rep_s(i, 1, m + 1) {
        rep_e(e, d[i]) { pq.push(e); }
        if (pq.size() > 0) {
            ans += pq.top();
            pq.pop();
        }
    }
    cout << ans << "\n";

    return 0;
}