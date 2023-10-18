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
    vector<ll> a(2 * n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    ll tot = 0;
    rep(i, n) {
        a[n + i] = a[i];
        tot += a[i];
    }

    bool ans = false;
    ll r = 0;
    ll now = 0;
    rep(l, 2 * n) {
        while (r < 2 * n and tot >= 10 * (now + a[r])) {
            now += a[r];
            r++;
        }
        if (tot == 10 * now) ans = true;
        if (l < r) {
            now -= a[l];
        } else {
            r++;
        }
    }
    cout << (ans ? "Yes" : "No") << "\n";
    return 0;
}