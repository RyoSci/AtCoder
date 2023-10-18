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
    ll n, q;
    cin >> n >> q;
    vector<ll> x(q), y(q), z(q), w(q);
    for (ll i = 0; i < q; i++) cin >> x[i] >> y[i] >> z[i] >> w[i];

    mint ans = 1;
    rep(i, 60) {
        ll res = 0;
        rep(j, 1 << n) {
            vector<ll> a(n);
            rep(k, n) {
                if (j >> k & 1) {
                    a[k] = 1;
                } else {
                    a[k] = 0;
                }
            }
            bool flag = true;
            rep(k, q) {
                if ((a[x[k] - 1] | a[y[k] - 1] | a[z[k] - 1]) ==
                    (w[k] >> i & 1)) {
                    continue;
                } else
                    flag = false;
            }
            if (flag) res++;
        }
        ans *= res;
        // cout << i << ' ' << res << ' ' << ans.val() << "\n";
    }
    cout << ans.val() << "\n";
    return 0;
}