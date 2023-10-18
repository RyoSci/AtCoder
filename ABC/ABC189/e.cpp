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
    ll n;
    cin >> n;
    vector<ll> x(n, 0), y(n, 0);
    rep(i, n) cin >> x[i] >> y[i];

    ll m;
    cin >> m;
    vector<P> op(m);
    for (ll i = 0; i < m; i++) {
        cin >> op[i].first;
        if (op[i].first <= 2) {
            op[i].second = -1;
        } else {
            cin >> op[i].second;
        }
    }

    ll q;
    cin >> q;
    vector<vector<P>> ab(m + 1);

    for (ll i = 0; i < q; i++) {
        ll a, b;
        cin >> a >> b;
        b--;
        ab[a].emplace_back(b, i);
    }

    ll ox = 0;
    ll oy = 0;
    bool flag = 0;
    bool px = 0;
    bool py = 0;
    vector<P> ans(q);
    rep(i, m + 1) {
        for (auto [b, i] : ab[i]) {
            ll bx = x[b];
            ll by = y[b];
            if (px) bx *= -1;
            if (py) by *= -1;
            if (flag) swap(bx, by);
            ans[i] = P(ox + bx, oy + by);
        }

        if (op[i].first == 1) {
            flag ^= 1;
            if (flag)
                px ^= 1;
            else
                py ^= 1;
            ll tmp = ox;
            ox = oy;
            oy = -tmp;
        }
        if (op[i].first == 2) {
            flag ^= 1;
            if (flag)
                py ^= 1;
            else
                px ^= 1;
            ll tmp = ox;
            ox = -oy;
            oy = tmp;
        }
        if (op[i].first == 3) {
            if (flag)
                py ^= 1;
            else
                px ^= 1;
            ox = op[i].second + op[i].second - ox;
        }
        if (op[i].first == 4) {
            if (flag)
                px ^= 1;
            else
                py ^= 1;
            oy = op[i].second + op[i].second - oy;
        }
    }

    for (auto a : ans) {
        cout << a.first << " " << a.second;
        cout << endl;
    }
    return 0;
}