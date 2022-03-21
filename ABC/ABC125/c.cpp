// #define _GLIBCXX_DEBUG
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

ll gcd(ll a, ll b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }

int main() {
    ll n;
    cin >> n;
    // n = 100000;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    // rep(i, n) { a[i] = 1e9 - i; }
    ll tot = 1;
    rep(i, n) { tot = lcm(tot, a[i]); }

    vector<ll> l(n + 1, tot);
    vector<ll> r(n + 1, tot);

    rep(i, n) { l[i + 1] = gcd(l[i], a[i]); }

    rep_r(i, n - 1, -1) { r[i] = gcd(r[i + 1], a[i]); }

    ll ans = 1;
    rep(i, n) { ans = max(ans, gcd(l[i], r[i + 1])); }

    cout << ans << "\n";
    return 0;
}