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
    ll n, m;
    cin >> n >> m;
    vector<ll> p(m);
    for (ll i = 0; i < m; i++) {
        cin >> p[i];
        p[i]--;
    }
    vector<ll> a(n - 1), b(n - 1), c(n - 1);
    rep(i, n - 1) { cin >> a[i] >> b[i] >> c[i]; }

    vector<ll> imos(n, 0);
    rep(i, m - 1) {
        ll start = p[i];
        ll end = p[i + 1];
        if (start > end) swap(start, end);
        imos[start]++;
        imos[end]--;
    }
    rep(i, n - 2) { imos[i + 1] += imos[i]; }
    ll ans = 0;
    rep(i, n - 1) { ans += min(imos[i] * a[i], c[i] + imos[i] * b[i]); }

    cout << ans << "\n";
    return 0;
}