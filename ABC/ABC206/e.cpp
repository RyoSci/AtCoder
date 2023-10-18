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
    vector<ll> cnt(r + 1, 0);

    rep_r(g, r, 1) {
        ll tmp = r / g - (l + g - 1) / g + 1;
        tmp *= tmp;
        for (ll gg = 2 * g; gg < r + 1; gg += g) {
            tmp -= cnt[gg];
        }
        cnt[g] = tmp;
        ans += tmp;
    }

    rep_s(g, 2, r + 1) {
        if (l <= g and g <= r) {
            ll tmp = r / g - (l + g - 1) / g + 1;
            ans -= tmp * 2;
            ans++;
        }
    }
    cout << ans << "\n";
    return 0;
}