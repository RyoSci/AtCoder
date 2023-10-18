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
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> x(n), y(n), z(n);
    rep(i, n) cin >> x[i] >> y[i] >> z[i];

    ll ans = 0;
    rep(i, 1 << n) {
        ll a = 0, b = 0, c = 0, cnt = 0;
        rep(j, n) {
            if (i >> j & 1) {
                a += x[j];
                b += y[j];
                c += z[j];
                cnt++;
            }
        }
        if (cnt == m && abs(a) + abs(b) + abs(c) > ans)
            ans = abs(a) + abs(b) + abs(c);
    }

    cout << ans << "\n";
    return 0;
}