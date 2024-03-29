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
// using lli = long long;
// using mint = modint1000000007;
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

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    // dp[i] = iの長さの右端
    vector<ll> dp(n + 1, INF);
    rep(i, n) {
        auto iter = lower_bound(dp.begin(), dp.end(), a[i]);
        auto dis = distance(dp.begin(), iter);
        // cout << *iter << " " << dis << "\n";
        dp[dis] = a[i];
        // for (auto a : dp) cout << a << " ";
        // cout << endl;
    }

    cout << lower_bound(dp.begin(), dp.end(), INF) - dp.begin() << "\n";
    // 下手
    // rep(i, n + 1) {
    //     if (dp[i] == INF) {
    //         cout << i << "\n";
    //         return 0;
    //     }
    // }
    return 0;
}