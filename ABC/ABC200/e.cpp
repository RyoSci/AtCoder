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
    ll n, k;
    cin >> n >> k;

    auto c2 = [&](ll x) {
        if (x < 0) return 0ll;
        return x * (x - 1) / 2;
    };

    auto f = [&](ll s) {
        ll res = c2(s - 3 + 2);
        ll dis = 0;
        dis += c2(s - 3 + 2 - n) * 3;
        dis -= c2(s - 3 + 2 - 2 * n) * 3;
        dis += c2(s - 3 + 2 - 3 * n);

        return res - dis;
    };

    auto f2 = [&](ll s) {
        ll l = max(1, s - n);
        ll r = min(n, s - 1);
        if (l > r) return 0ll;
        ll res = r - l + 1;
        return res;
    };

    rep_s(tot, 3, 3 * n + 1) {
        ll s = f(tot);
        if (s >= k) {
            rep_s(a, 1, n + 1) {
                s = f2(tot - a);
                if (s >= k) {
                    rep_s(b, 1, n + 1) {
                        ll c = tot - a - b;
                        if (0 < c and c < n + 1) {
                            if (k == 1) {
                                cout << a << ' ' << b << ' ' << c << "\n";
                                return 0;
                            }
                            k--;
                        }
                    }
                } else
                    k -= s;
            }
        } else
            k -= s;
    }
    return 0;
}