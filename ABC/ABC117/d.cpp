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

void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> cnt(60, 0);
    rep(i, n) {
        ll now = a[i];
        ll j = 0;
        while (now > 0) {
            cnt[j] += now % 2;
            now /= 2;
            j++;
        }
    }
    vector<ll> xs(60, 0);
    ll x = k;
    ll j = 0;
    while (x > 0) {
        xs[j] = x % 2;
        x /= 2;
        j++;
    }
    reverse(cnt.begin(), cnt.end());
    reverse(xs.begin(), xs.end());
    vector<vector<ll>> dp(61, vector<ll>(2, -1));
    // dp[i][j]:=i桁目まで各桁を取るか決めて、kより小さく自由にとっていいかどうかT/F(j)
    dp[0][0] = 0;
    rep(i, 60) {
        ll one = (n - cnt[i]) * powl(2, 60 - 1 - i);
        ll zero = (cnt[i]) * powl(2, 60 - 1 - i);
        if (xs[i] == 1) {
            chmax(dp[i + 1][1], dp[i][0] + zero);
            if (cnt[i] < n - cnt[i]) {
                chmax(dp[i + 1][0], dp[i][0] + one);
                if (dp[i][1] != -1) chmax(dp[i + 1][1], dp[i][1] + one);
            } else {
                chmax(dp[i + 1][0], dp[i][0] + zero);
                if (dp[i][1] != -1) chmax(dp[i + 1][1], dp[i][1] + zero);
            }
        } else {
            chmax(dp[i + 1][0], dp[i][0] + zero);
            if (cnt[i] < n - cnt[i]) {
                if (dp[i][1] != -1) chmax(dp[i + 1][1], dp[i][1] + one);
            } else {
                if (dp[i][1] != -1) chmax(dp[i + 1][1], dp[i][1] + zero);
            }
        }
    }

    cout << max(dp[60][0], dp[60][1]) << "\n";
    // rep(i, 61) {
    //     for (auto a : dp[i]) cout << a << " ";
    //     cout << endl;
    // }
    // for (auto a : xs) cout << a << " ";
    // cout << endl;
    return 0;
}