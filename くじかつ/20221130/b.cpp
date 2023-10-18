// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
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
// using mint = modint1000000007;
using mint = modint998244353;
// #define MOD 1000000007
#define MOD 998244353
#define INF (1LL << 60)
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
    vector<ll> t(n, 0), l(n, 0), r(n, 0);
    rep(i, n) cin >> t[i] >> l[i] >> r[i];

    ll ans = 0;
    rep(i, n) {
        ll li = l[i] * 10, ri = r[i] * 10;
        if (t[i] == 2 or t[i] == 4) ri -= 5;
        if (t[i] == 3 or t[i] == 4) li += 5;
        rep_s(j, i + 1, n) {
            ll lj = l[j] * 10, rj = r[j] * 10;
            if (t[j] == 2 or t[j] == 4) rj -= 5;
            if (t[j] == 3 or t[j] == 4) lj += 5;

            if (!(rj < li or ri < lj)) ans++;
        }
    }
    cout << ans << "\n";
    return 0;
}