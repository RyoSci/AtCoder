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

bool is_prime(ll x) {
    for (ll i = 2; i * i <= x; i++) {
        if (x % i == 0) return false;
    }
    return true;
}

ll gcd(ll x, ll y) {
    if (y == 0) return x;
    return gcd(y, x % y);
}

int main() {
    ll l, r;
    cin >> l >> r;
    // 素数砂漠確認
    // rep_r(u, powl(10, 18), powl(10, 18) - 1000) {
    //     if (is_prime(u)) {
    //         cout << u << "\n";
    //     }
    // }
    ll ans = 0;
    for (ll i = l; i <= min(l + 1000, r); i++) {
        for (ll j = r; j >= max(r - 1000, l); j--) {
            if (i < j && gcd(i, j) == 1) ans = max(ans, j - i);
        }
    }
    cout << ans << "\n";
    return 0;
}