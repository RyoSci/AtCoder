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
    vector<ll> a(n), b(n);
    for (ll i = 0; i < n; i++) cin >> a[i] >> b[i];

    set<ll> tree;
    tree.insert(INF);
    rep(i, m) { tree.insert(i + 1); }

    vector<P> c;
    rep(i, n) { c.push_back(make_pair(-b[i], a[i])); }
    sort(c.begin(), c.end());

    ll ans = 0;
    ll bi, ai;
    rep(i, n) {
        bi = c[i].first;
        bi = -bi;
        ai = c[i].second;
        auto iter = tree.lower_bound(ai);
        if (*iter == INF)
            continue;
        else {
            ans += bi;
            tree.erase(*iter);
        }
    }
    cout << ans << "\n";
    return 0;
}