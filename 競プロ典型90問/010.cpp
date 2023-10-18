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
    vector<ll> c(n), p(n);
    for (ll i = 0; i < n; i++) cin >> c[i] >> p[i];
    vector<ll> a(n + 1, 0), b(n + 1, 0);

    rep(i, n) {
        if (c[i] == 1)
            a[i + 1] = p[i];
        else
            b[i + 1] = p[i];
    }

    rep(i, n) {
        a[i + 1] += a[i];
        b[i + 1] += b[i];
    }

    ll q;
    cin >> q;
    rep(i, q) {
        ll l, r;
        cin >> l >> r;
        cout << a[r] - a[l - 1] << "\n";
        cout << b[r] - b[l - 1] << "\n";
    }

    // for (auto a : a) cout << a << " ";
    // cout << endl;
    // for (auto a : b) cout << a << " ";
    // cout << endl;
    return 0;
}