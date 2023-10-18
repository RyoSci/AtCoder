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

ll e2t(ll x) {
    ll res = 0;
    ll keta = 1;
    while (x > 0) {
        res += (x % 10) * keta;
        keta *= 8;
        x /= 10;
    }
    return res;
}

ll t2n(ll x) {
    ll res = 0;
    ll keta = 1;
    while (x > 0) {
        if (x % 9 == 8)
            res += 5 * keta;
        else
            res += (x % 9) * keta;
        x /= 9;
        keta *= 10;
    }
    return res;
}

int main() {
    ll n, k;
    cin >> n >> k;
    rep(i, k) {
        n = e2t(n);
        n = t2n(n);
    }
    cout << n << "\n";

    return 0;
}