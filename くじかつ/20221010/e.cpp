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
    ll n;
    cin >> n;
    vector<vector<ll>> p(n), e(n);

    map<ll, vector<ll>> ps;

    rep(i, n) {
        ll m;
        cin >> m;
        rep(j, m) {
            ll pj, ej;
            cin >> pj >> ej;
            p[i].emplace_back(pj);
            e[i].emplace_back(ej);
            if (ps[pj].size() == 0) ps[pj].emplace_back(0);
            ps[pj].emplace_back(ej);
        }
    }

    rep_e(e, ps) sort(ps[e.first].rbegin(), ps[e.first].rend());

    set<vector<P>> ans;
    rep(i, n) {
        vector<P> tmp;
        rep(j, p[i].size()) {
            if (ps[p[i][j]][0] == e[i][j]) {
                if (ps[p[i][j]][1] != e[i][j]) {
                    tmp.emplace_back(P(p[i][j], ps[p[i][j]][1]));
                }
            }
        }
        ans.insert(tmp);
    }

    cout << ans.size() << "\n";
    return 0;
}