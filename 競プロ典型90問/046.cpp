// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
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
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> b(n);
    for (ll i = 0; i < n; i++) cin >> b[i];
    vector<ll> c(n);
    for (ll i = 0; i < n; i++) cin >> c[i];

    vector<ll> da(46), db(46), dc(46);
    rep(i, n) {
        da[a[i] % 46]++;
        db[b[i] % 46]++;
        dc[c[i] % 46]++;
    }
    ll ans = 0;
    rep(i, 46) rep(j, 46) rep(k, 46) {
        if ((i + j + k) % 46 == 0) {
            ll tmp = da[i] * db[j] * dc[k];
            ans += tmp;
        }
    }

    cout << ans << "\n";

    return 0;
}