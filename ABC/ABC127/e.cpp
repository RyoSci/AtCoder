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
#define MOD 1000000007
// #define MOD 998244353
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
    ll n, m, k;
    cin >> n >> m >> k;

    vector<mint> frac(n * m + 1, 0);
    vector<mint> invfrac(n * m + 1, 0);
    frac[0] = 1;
    rep(i, n * m) frac[i + 1] = frac[i] * (i + 1);
    invfrac[0] = 1;
    invfrac[n * m] = mint(frac[n * m]).pow(MOD - 2);
    rep_r(i, n * m, 0) invfrac[i - 1] = invfrac[i] * i;

    auto combinations = [&](ll n, ll k) {
        if (k < 0 | n < k) return mint(0);
        return frac[n] * invfrac[k] * invfrac[n - k];
    };

    mint ans = 0;
    vector<ll> x, y;
    rep(i, n) {
        rep(j, m) {
            x.emplace_back(i + 1);
            y.emplace_back(j + 1);
        }
    }

    sort(x.begin(), x.end());
    sort(y.begin(), y.end());

    vector<ll> totx(n * m + 1, 0);
    vector<ll> toty(n * m + 1, 0);
    rep(i, n * m) totx[i + 1] += totx[i] + x[i];
    rep(i, n * m) toty[i + 1] += toty[i] + y[i];

    rep(i, n) {
        rep(j, m) {
            auto pos = upper_bound(x.begin(), x.end(), i + 1) - x.begin();
            ll tmp = (i + 1) * (pos - 1) - (totx[pos - 1] - totx[0]);
            tmp += totx[n * m] - totx[pos] - (i + 1) * (n * m - pos);

            pos = upper_bound(y.begin(), y.end(), j + 1) - y.begin();
            tmp += (j + 1) * (pos - 1) - (toty[pos - 1] - toty[0]);
            tmp += toty[n * m] - toty[pos] - (j + 1) * (n * m - pos);
            ans += tmp * combinations(n * m - 2, k - 2);
        }
    }
    ans /= 2;
    cout << ans.val() << "\n";
    return 0;
}