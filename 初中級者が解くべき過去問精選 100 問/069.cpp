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

int main() {
    ll q;
    cin >> q;
    ll n = 100000;
    vector<ll> a(n + 1, 1);
    a[0] = 0;
    a[1] = 0;
    rep_s(i, 2, n) {
        if (!a[i]) continue;
        for (ll j = 2 * i; j < n + 1; j += i) {
            a[j] = 0;
        }
    }

    vector<ll> b(n + 1, 0);
    rep(i, n + 1) {
        if (i % 2 == 1 && a[i] && a[(i + 1) / 2]) b[i]++;
    }
    rep(i, n) { b[i + 1] += b[i]; }

    ll ans = 0;
    rep(i, q) {
        ll l, r;
        cin >> l >> r;
        ans = b[r] - b[l - 1];
        cout << ans << "\n";
    }
    return 0;
}