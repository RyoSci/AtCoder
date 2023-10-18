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

ll pow_ll(ll n, ll p) {
    ll res = 1;
    while (p) {
        if (p % 2 == 1) res *= n;
        n *= n;
        p >>= 1;
    }
    return res;
}

int main() {
    ll n;
    cin >> n;
    vector<ll> x(n), y(n);
    rep(i, n) { cin >> x[i] >> y[i]; }
    double ans = 0.0;
    rep(i, n) rep_s(j, i + 1, n) {
        ans += sqrt(pow_ll(x[i] - x[j], 2) + pow_ll(y[i] - y[j], 2));
    }
    //小数点以下の長さを指定
    cout << fixed << setprecision(15) << 2.0 * ans / n << endl;
    return 0;
}