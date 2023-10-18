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
        ll n, q;
        cin >> n >> q;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        ll odd = 0;
        ll even = 0;
        ll ans = 0;
        rep(i, n) {
            if (a[i] % 2 == 0)
                even++;
            else
                odd++;
            ans += a[i];
        }
        rep(i, q) {
            ll op, num;
            cin >> op >> num;
            if (op == 0) {
                ans += num * even;
                if (num % 2 == 1) {
                    odd += even;
                    even = 0;
                }
            } else {
                ans += num * odd;
                if (num % 2 == 1) {
                    even += odd;
                    odd = 0;
                }
            }
            cout << ans << "\n";
        }
    }
    return 0;
}