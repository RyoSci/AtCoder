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
    ll n, k;
    cin >> n >> k;
    vector<ll> l(k, 0), r(k, 0);
    rep(i, k) cin >> l[i] >> r[i];

    vector<mint> tot(k, 0);

    vector<mint> dp(n, 0);
    dp[0] = 1;

    rep(i, n) {
        rep(j, k) {
            ll R = i - l[j];
            ll L = i - r[j];
            if (0 <= R) tot[j] += dp[R];
            if (1 <= L) tot[j] -= dp[L - 1];
            dp[i] += tot[j];
        }
    }

    cout << dp[n - 1].val() << "\n";

    return 0;
}