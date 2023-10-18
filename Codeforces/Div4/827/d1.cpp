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

ll gcd(ll x, ll y) {
    if (y == 0) return x;
    return gcd(y, x % y);
}

int main() {
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];

        vector<vector<ll>> can_pair(1001);
        rep_s(i, 1, 1001) {
            rep_s(j, 1, 1001) {
                if (gcd(i, j) == 1) can_pair[i].emplace_back(j);
            }
        }

        vector<ll> max_pos(1001, -1);

        rep(i, n) { max_pos[a[i]] = i; }

        ll ans = -1;
        rep(i, 1001) {
            if (max_pos[i] != -1) {
                rep_e(e, can_pair[i]) {
                    if (max_pos[e] != -1)
                        ans = max(ans, max_pos[i] + max_pos[e] + 2);
                }
            }
        }
        cout << ans << "\n";
    }
    return 0;
}