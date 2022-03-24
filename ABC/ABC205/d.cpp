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
    ll n, q;
    cin >> n >> q;
    vector<ll> a(n + 2);
    for (ll i = 0; i < n; i++) cin >> a[i + 1];
    a[0] = 0;
    a[n + 1] = INF + 10000000;
    vector<P> k(q);
    for (ll i = 0; i < q; i++) {
        cin >> k[i].first;
        k[i].second = i;
    }
    sort(k.begin(), k.end());

    ll now = 0;
    vector<ll> ans(q);

    rep(i, q) {
        ll l, r;
        l = a[now];
        r = a[now + 1];
        ll tmp = now + k[i].first;

        while (!(l < tmp && tmp < r)) {
            now++;
            l = a[now];
            r = a[now + 1];
            tmp = now + k[i].first;
        }

        ans[k[i].second] = k[i].first + now;
    }

    rep(i, q) { cout << ans[i] << "\n"; }
    return 0;
}