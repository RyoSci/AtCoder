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
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> s(n);
    for (ll i = 0; i < n; i++) cin >> s[i];

    rep(i, n) {
        if (s[i] == 0) {
            cout << n << "\n";
            return 0;
        }
    }

    ll r = 0;
    ll now = 1;
    ll ans = 0;
    rep(l, n) {
        r = max(r, l);
        while (r < n and now * s[r] <= k) {
            now *= s[r];
            r++;
        }
        ans = max(ans, r - l);
        if (l != r) now /= s[l];
    }
    cout << ans << "\n";
    return 0;
}