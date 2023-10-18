#define _GLIBCXX_DEBUG
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

vector<ll> x, y;

ll f(ll i, ll ax, ll ay) {
    ll dx = x[i] - x[i + 1];
    ll dy = y[i] - y[i + 1];
    return dx * (ay - y[i]) - dy * (ax - x[i]);
}

ll g(ll i, ll ax, ll ay, ll bx, ll by) {
    ll dx = ax - bx;
    ll dy = ay - by;
    return dx * (y[i] - ay) - dy * (x[i] - ax);
}

int main() {
    ll ax, ay, bx, by;
    cin >> ax >> ay >> bx >> by;
    ll n;
    cin >> n;
    x.resize(n + 1);
    y.resize(n + 1);
    for (ll i = 0; i < n; i++) cin >> x[i] >> y[i];
    x[n] = x[0];
    y[n] = y[0];

    ll cnt = 0;
    rep(i, n) {
        if (f(i, ax, ay) * f(i, bx, by) < 0 &&
            g(i, ax, ay, bx, by) * g(i + 1, ax, ay, bx, by) < 0)
            cnt++;
    }

    cout << cnt / 2 + 1 << "\n";
    return 0;
}