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
    ll n, h;
    cin >> n >> h;
    ll a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;
    ll ans = INF;
    rep(i, n + 1) {
        ll rest = n - i;
        ll hp = h - i * e;

        if (rest * d + hp > 0) {
            ans = min(ans, rest * c);
        } else if (rest * b + hp <= 0) {
            continue;
        } else {
            ll ng = 0, ok = rest;
            while (ng + 1 < ok) {
                ll mid = (ng + ok) / 2;
                if (hp + mid * b + (rest - mid) * d > 0)
                    ok = mid;
                else
                    ng = mid;
            }
            ans = min(ans, ok * a + (rest - ok) * c);
        }
    }

    cout << ans << "\n";
    return 0;
}