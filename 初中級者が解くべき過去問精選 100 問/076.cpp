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
    ll n;
    cin >> n;
    vector<ll> a(n + 1);
    for (ll i = 1; i < n + 1; i++) cin >> a[i];
    rep(i, n) { a[i + 1] += a[i]; }
    vector<ll> ans(n + 1, 0);

    rep(i, n) {
        rep_s(j, i + 1, n + 1) { ans[j - i] = max(ans[j - i], a[j] - a[i]); }
    }
    rep(i, n) { cout << ans[i + 1] << "\n"; }
    return 0;
}