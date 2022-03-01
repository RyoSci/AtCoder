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
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG

ll find(ll x, vector<ll> &par) {
    if (par[x] < 0) return x;
    return par[x] = find(par[x], par);
}

void unite(ll x, ll y, vector<ll> &par) {
    ll px = find(x, par);
    ll py = find(y, par);
    if (px == py) return;
    par[px] += par[py];
    par[py] = px;
    return;
}

bool same(ll x, ll y, vector<ll> &par) { return find(x, par) == find(y, par); }

int main() {
    while (1) {
        ll n;
        cin >> n;
        if (n == 0) return 0;
        vector<ll> par(n, -1);
        vector<double> x(n), y(n), z(n), r(n);
        rep(i, n) { cin >> x[i] >> y[i] >> z[i] >> r[i]; }

        // まず重なりがあるかどうかを確認する
        rep(i, n) {
            rep(j, n) {
                if (pow(x[i] - x[j], 2.0) + pow(y[i] - y[j], 2.0) +
                        pow(z[i] - z[j], 2.0) <=
                    pow(r[i] + r[j], 2.0))
                    unite(i, j, par);
            }
        }

        // 辺をはる
        vector<tuple<double, ll, ll>> edges;
        rep(i, n - 1) {
            rep_s(j, i + 1, n) {
                double dis = pow(pow(x[i] - x[j], 2.0) + pow(y[i] - y[j], 2.0) +
                                     pow(z[i] - z[j], 2.0),
                                 0.5);
                dis = dis - r[i] - r[j];
                if (dis > 0) edges.push_back(make_tuple(dis, i, j));
            }
        }

        double ans = 0.0;
        // つなげていく
        sort(edges.begin(), edges.end());
        rep(i, edges.size()) {
            double dis;
            ll a, b;
            tie(dis, a, b) = edges[i];
            if (same(a, b, par))
                continue;
            else {
                unite(a, b, par);
                ans += dis;
            }
        }
        //小数点以下の長さを指定
        cout << fixed << setprecision(3) << ans << endl;
    }
    return 0;
}