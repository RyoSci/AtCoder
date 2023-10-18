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

    ll m = 3 * n;
    vector<mint> frac;
    vector<mint> invfrac;
    frac.resize(m + 1);
    invfrac.resize(m + 1);

    frac[0] = 1;
    rep(i, m) frac[i + 1] = frac[i] * (i + 1);
    invfrac[0] = 1;
    rep(i, m) invfrac[i + 1] = invfrac[i] / (i + 1);

    auto combination = [&](ll m, ll k) -> mint {
        if (m < k) return 0;
        if (m < 0 || k < 0) return 0;
        return frac[m] * invfrac[k] * invfrac[m - k];
    };
    mint ans = 0;
    rep_s(i, 0, min(n, k) + 1) {
        ll rest = n - i;
        mint res;
        res = combination(n, i);
        res *= combination(i + rest - 1, i);
        ans += res;
    }

    cout << ans.val() << "\n";
    return 0;
}