#include <algorithm>
// #include <atcoder/all>
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
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG

int main() {
    ll n, q;
    cin >> n >> q;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> c(q + 2);
    for (ll i = 1; i < q + 1; i++) cin >> c[i];
    c[0] = 1;
    c[q + 1] = 1;

    vector<mint> memo(n, 0);
    rep(i, n - 1) {
        mint tmp = a[i];
        memo[i + 1] = tmp.pow(a[i + 1]);
    }
    rep(i, n - 1) { memo[i + 1] += memo[i]; }

    mint ans = 0;
    rep(i, q + 1) {
        mint tmp = 0;
        if (c[i + 1] > c[i]) {
            tmp = memo[c[i + 1] - 1] - memo[c[i] - 1];
            ans += tmp;
        } else {
            tmp = memo[c[i] - 1] - memo[c[i + 1] - 1];
            ans += tmp;
        }
    }
    cout << ans.val() << "\n";
    return 0;
}