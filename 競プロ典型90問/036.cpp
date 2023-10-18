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
    ll n, q;
    cin >> n >> q;
    vector<ll> x(n), y(n);
    for (ll i = 0; i < n; i++) cin >> x[i] >> y[i];

    rep(i, n) {
        ll tmpx = x[i];
        x[i] = tmpx + y[i];
        y[i] = tmpx - y[i];
    }

    vector<ll> xx, yy;
    xx = x;
    yy = y;

    sort(xx.begin(), xx.end());
    sort(yy.begin(), yy.end());

    rep(i, q) {
        ll qi;
        cin >> qi;
        qi--;
        ll ans = 0;
        ans = max(ans, abs(xx[n - 1] - x[qi]));
        ans = max(ans, abs(xx[0] - x[qi]));
        ans = max(ans, abs(yy[n - 1] - y[qi]));
        ans = max(ans, abs(yy[0] - y[qi]));
        cout << ans << "\n";
    }

    return 0;
}