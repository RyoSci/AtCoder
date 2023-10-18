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
    ll l, r;
    cin >> l >> r;
    ll ans = 0;
    for (ll g = 2; g <= r; g++) {
        for (ll i = 2; g * i <= r; i++) {
            // if (g * i < l) continue;
            ll ri = r / g;
            ll li = (l + g - 1) / g;
            ll rj = r / g / i;
            ll lj = (l + g * i - 1) / g / i;

            // ans += ri - li + 1 - (rj - lj + 1);
            // cout << g << ' ' << i << ' ' << ri << ' ' << li << ' ' << rj << '
            // '
            //      << lj << ' ' << ans << "\n";
            ans += (ri - max(li, i) + 1 - (rj - lj + 1)) * 2;
        }
    }
    cout << ans << "\n";
    return 0;
}