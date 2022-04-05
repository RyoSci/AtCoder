// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
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
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

vector<mint> memo(100100);
vector<mint> rmemo(100100);

mint nCk(ll n, ll k) {
    if (n < k | k < 0) return 0;
    mint res;
    res = memo[n] * rmemo[n - k] * rmemo[k];
    return res;
}

// x^(p-2)を求める
mint inv(mint x) {
    return x.pow(MOD - 2);
    // ll p = MOD - 2;
    // mint rest = 1;
    // while (p > 1) {
    //     if (p % 2 == 1) {
    //         rest *= x;
    //         // rest %= MOD;
    //     }
    //     p /= 2;
    //     x = x * x;
    //     // x %= MOD;
    // }
    // return x * rest;
    // return x * rest % MOD;
}

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    sort(a.begin(), a.end());

    memo[0] = 1;
    rep_s(i, 1, 100100) {
        memo[i] = memo[i - 1] * i;
        // memo[i] %= MOD;
    }
    rep_s(i, 0, 100100) { rmemo[i] = inv(memo[i]); }

    if (k == 1) {
        cout << 0 << "\n";
        return 0;
    }
    mint ans = 0;
    // ll ans = 0;
    rep_s(i, k, n) {
        mint cnt = nCk(i, k - 1);
        ans += a[i] * cnt;
        // ans += a[i] * memo[i] * rmemo[k - 1] * rmemo[i - (k - 1)];
        // ans += a[i] * nCk(i, k - 1);
        // ans %= MOD;
    }
    rep_s(i, 0, n - k + 1) {
        mint cnt = nCk(n - 1 - i, k - 1);
        ans -= a[i] * cnt;
        // ans -=
        //     a[i] * memo[n - 1 - i] * rmemo[k - 1] * rmemo[n - 1 - i - (k -
        //     1)];
        // ans -= a[i] * nCk(n - 1 - i, k - 1);
        // ans %= MOD;
    }

    // cout << (ans + MOD) % MOD << "\n";
    cout << ans.val() << "\n";
    return 0;
}