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
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    ll m = 0, p = 0;
    vector<ll> ps, ms;
    rep(i, n) {
        if (a[i] < 0) {
            m++;
            ms.emplace_back(a[i]);
        } else {
            p++;
            ps.emplace_back(a[i]);
        }
    }
    ll rest = max(k % 2, k - m / 2 * 2);
    mint ans = 1;
    if (rest <= p) {
        sort(ps.begin(), ps.end());
        sort(ms.begin(), ms.end());
        reverse(ps.begin(), ps.end());
        // reverse(ms.begin(), ms.end());
        vector<ll> tot;

        if (rest % 2 == 1) {
            ans *= ps[0];
            for (ll i = 1; i < ps.size(); i += 2) {
                tot.emplace_back(ps[i] * ps[i + 1]);
            }
        } else {
            for (ll i = 0; i < ps.size(); i += 2) {
                tot.emplace_back(ps[i] * ps[i + 1]);
            }
        }

        for (ll i = 0; i < ms.size(); i += 2) {
            tot.emplace_back(ms[i] * ms[i + 1]);
        }

        sort(tot.begin(), tot.end());
        reverse(tot.begin(), tot.end());
        rep(i, k / 2) ans *= tot[i];

    } else {
        rep(i, n) a[i] = abs(a[i]);
        sort(a.begin(), a.end());
        rep(i, k) ans *= a[i];
        ans = -ans;
    }

    cout << ans.val() << "\n";
    return 0;
}