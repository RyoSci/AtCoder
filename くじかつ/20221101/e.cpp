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

ll n;

vector<mint> frac;
vector<mint> invfrac;

mint combination(ll n, ll k) {
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return frac[n] * invfrac[k] * invfrac[n - k];
}

int main() {
    string s;
    cin >> s;
    n = s.size();
    frac.resize(n + 1);
    invfrac.resize(n + 1);

    frac[0] = 1;
    rep(i, n) frac[i + 1] = frac[i] * (i + 1);
    invfrac[0] = 1;
    rep(i, n) invfrac[i + 1] = invfrac[i] / (i + 1);

    vector<vector<mint>> dp(27, vector<mint>(n + 1, 0));
    dp[0][0] = 1;

    vector<ll> cnt(26, 0);
    rep(i, n) cnt[s[i] - 'a']++;

    rep(i, 26) {
        rep(j, n + 1) {
            rep(k, cnt[i] + 1) {
                if (j + k <= n) {
                    dp[i + 1][j + k] += dp[i][j] * combination(j + k, k);
                    // cout << i << ' ' << j << ' ' << k << "\n";
                    // cout << combination(j + k, k).val() << "\n";
                    // cout << dp[i][j].val() << "\n";
                }
            }
        }
    }

    mint ans = 0;
    rep(i, n) ans += dp[26][i + 1];
    cout << ans.val() << "\n";

    return 0;
}