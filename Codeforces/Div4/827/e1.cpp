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
// #define INF (1L << 60)
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
        vector<P> k(q);
        for (ll i = 0; i < q; i++) {
            cin >> k[i].first;
            k[i].second = i;
        }

        vector<ll> h(n + 1, 0);
        rep(i, n) h[i + 1] = a[i];
        rep(i, n - 1) h[i + 2] += h[i + 1];

        vector<ll> ans(q);
        sort(k.begin(), k.end());
        ll j = -1;
        rep(i, q) {
            auto [kk, ki] = k[i];
            while (a[j + 1] <= kk and j + 1 < n) {
                j++;
            }
            ans[ki] = h[j + 1];
        }
        for (auto a : ans) cout << a << " ";
        cout << endl;
    }
    return 0;
}