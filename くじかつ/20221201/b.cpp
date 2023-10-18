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
    ll n, k;
    cin >> n >> k;
    vector<ll> a(k);
    for (ll i = 0; i < k; i++) cin >> a[i];
    vector<ll> x(n, 0), y(n, 0);
    rep(i, n) cin >> x[i] >> y[i];

    auto cal = [&](ll a, ll b, ll c, ll d) {
        double res = (a - c) * (a - c) + (b - d) * (b - d);
        res = sqrt(res);
        return res;
    };

    double ans = 0.0;
    rep(i, n) {
        double near = INF;
        rep(j, k) {
            double dis = cal(x[i], y[i], x[a[j] - 1], y[a[j] - 1]);
            near = min(near, dis);
        }
        ans = max(ans, near);
    }
    //小数点以下の長さを指定
    cout << fixed << setprecision(15) << ans << endl;
    return 0;
}