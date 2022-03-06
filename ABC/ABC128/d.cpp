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
    vector<ll> v(n);
    for (ll i = 0; i < n; i++) cin >> v[i];
    ll ans = 0;
    rep(l, n + 1) {
        rep_r(r, n, -1) {
            if (l > r || l + (n - r) > k) break;
            ll kk = k - (l + n - r);
            ll m = l + n - r;
            vector<ll> a;
            rep(i, l) { a.push_back(v[i]); }
            rep_s(i, r, n) { a.push_back(v[i]); }
            sort(a.begin(), a.end());
            rep(i, kk) {
                if (a.size() > i + 1 && a[i] < 0) a[i] = 0;
            }
            ll tmp = 0;
            rep_e(e, a) { tmp += e; }
            ans = max(ans, tmp);
        }
    }
    cout << ans << "\n";
    return 0;
}