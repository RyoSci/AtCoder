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
    vector<ll> a(n), t(n);
    rep(i, n) cin >> a[i] >> t[i];

    ll q;
    cin >> q;
    vector<ll> x(q);
    for (ll i = 0; i < q; i++) cin >> x[i];

    ll l = -INF;
    ll r = INF;
    ll now = 0;
    rep(i, n) {
        if (t[i] == 1) {
            now += a[i];
        } else if (t[i] == 2) {
            ll nl = a[i] - now;
            if (nl >= r) {
                l = r = nl;
            } else if (nl >= l) {
                l = nl;
            } else {
                //
            }
        } else {
            ll nr = a[i] - now;
            if (nr <= l) {
                l = r = nr;
            } else if (nr <= r) {
                r = nr;
            } else {
                //
            }
        }
    }

    ll ansl = l;
    ll ansr = r;
    rep(i, n) {
        if (t[i] == 1) {
            ansl += a[i];
            ansr += a[i];
        } else if (t[i] == 2) {
            ansl = max(ansl, a[i]);
            ansr = max(ansr, a[i]);
        } else {
            ansl = min(ansl, a[i]);
            ansr = min(ansr, a[i]);
        }
    }

    rep(i, q) {
        if (x[i] <= l) {
            cout << ansl << "\n";
        } else if (r <= x[i]) {
            cout << ansr << "\n";
        } else {
            cout << ansl + x[i] - l << "\n";
        }
    }
    return 0;
}