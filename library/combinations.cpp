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
// using mint = modint1000000007;
using mint = modint998244353;
#define MOD 998244353
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
    vector<mint> frac;
    vector<mint> invfrac;
    frac.resize(n + 1);
    invfrac.resize(n + 1);

    frac[0] = 1;
    rep(i, n) frac[i + 1] = frac[i] * (i + 1);
    invfrac[0] = 1;
    rep(i, n) invfrac[i + 1] = invfrac[i] / (i + 1);

    auto combination = [&](ll n, ll k) -> mint {
        if (n < k) return 0;
        if (n < 0 || k < 0) return 0;
        return frac[n] * invfrac[k] * invfrac[n - k];
    };
}