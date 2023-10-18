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
    vector<ll> a(m), b(m);
    for (ll i = 0; i < m; i++) cin >> a[i] >> b[i];

    vector<P> relations;
    rep(i, m) { relations.push_back(make_pair(b[i], a[i])); }
    sort(relations.begin(), relations.end());

    set<ll> del_bridges;
    del_bridges.insert(INF);
    rep(i, m) {
        ll bi, ai;
        tie(bi, ai) = relations[i];
        if (del_bridges.size() == 0) {
            del_bridges.insert(bi);
        } else {
            auto iter = del_bridges.upper_bound(ai);
            if (*iter == INF) {
                del_bridges.insert(bi);
            }
        }
    }
    cout << del_bridges.size() - 1 << "\n";
    return 0;
}