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
using mint = modint1000000007;
// using mint = modint998244353;
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
    ll n, k;
    cin >> n >> k;

    vector<mint> frac;
    vector<mint> invfrac;
    frac.resize(2 * n + 1);
    invfrac.resize(2 * n + 1);

    frac[0] = 1;
    rep(i, 2 * n) frac[i + 1] = frac[i] * (i + 1);
    invfrac[0] = 1;
    rep(i, 2 * n) invfrac[i + 1] = invfrac[i] / (i + 1);

    auto combination = [&](ll n, ll k) -> mint {
        if (n < k) return 0;
        if (n < 0 || k < 0) return 0;
        return frac[n] * invfrac[k] * invfrac[n - k];
    };

    ll rest;
    ll now;
    if (k >= n - 1) {
        rest = (k - (n - 1)) % 2;
        now = n - rest;
    } else {
        now = k + 1;
        rest = n - now;
    }

    mint ans = 0;
    rep(i, now + 1) {
        // ans += combination(n - 1 + rest - 1, rest);
        ans += frac[rest + n - 1 - 1] / frac[rest] / frac[n - 1 - 1];
        rest++;
    }

    cout << ans.val() << "\n";

    return 0;
}