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
using lli = long long;
// using mint = modint1000000007;
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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        vector<ll> a(n + 1);
        for (ll i = 1; i < n + 1; i++) cin >> a[i];
        rep(i, n) a[i + 1] += a[i];

        set<ll> s;
        rep(i, n + 1) s.insert(a[i]);

        ll m = a[n];
        vector<ll> div;
        for (ll i = 1; i * i <= m; i++) {
            if (m % i == 0) {
                div.emplace_back(i);
                if (m / i != i) div.emplace_back(m / i);
            }
        }
        sort(div.begin(), div.end());

        // for (auto a : s) cout << a << " ";
        // cout << endl;

        ll ans = n;
        rep_e(e, div) {
            if (m / e > n) continue;
            bool flag = true;
            rep(i, m / e) {
                if (s.count((i + 1) * e) != 0)
                    continue;
                else
                    flag = false;
            }
            // cout << e << " " << flag << "\n";
            if (flag) {
                ll l, r;
                l = 0;
                ll res = 0;
                rep(i, m / e) {
                    r = lower_bound(a.begin(), a.end(), (i + 1) * e) -
                        a.begin();
                    res = max(res, r - l);
                    // cout << l << ' ' << r << ' ' << res << "\n";
                    l = r;
                }
                ans = min(ans, res);
            }
        }
        cout << ans << "\n";
    }
    return 0;
}