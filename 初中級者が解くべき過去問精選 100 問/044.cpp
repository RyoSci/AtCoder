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
#define INF (1 << 29)
#define EPS (1e-10)
// typedef long long ll;
typedef int ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG

void chmin(ll& x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    vector<ll> odd, both;

    ll m = 1000000;
    for (ll i = 1; i * (i + 1) * (i + 2) / 6 <= m + 10; i++) {
        ll f = i * (i + 1) * (i + 2) / 6;
        if (f % 2 == 1) odd.push_back(f);
        both.push_back(f);
    }

    ll n = both.size();
    vector<ll> dp_both(m + 10, INF);
    // vector<vector<ll>> dp_both(n + 1, vector<ll>(m + 10, INF));
    // dp[i][j]<-i-1番目までの正四面体の取り方がわかっている時に、i番目の正四面体をいくつか取って合計数をjとする時の取った数の最小値
    // ナップザックdp 遷移はとるか撮らないか

    dp_both[0] = 0;
    // dp_both[0][0] = 0;
    rep_s(i, 1, n + 1) {
        rep(j, m + 1) {
            // 2次元DPの時
            // 使わない場合
            // chmin(dp_both[i][j], dp_both[i - 1][j]);

            // // 横に展開
            // if (j - both[i - 1] >= 0) {
            //     chmin(dp_both[i][j], dp_both[i][j - both[i - 1]] + 1);
            // }

            // 1次元DPの時
            // 横に展開
            if (j - both[i - 1] >= 0) {
                chmin(dp_both[j], dp_both[j - both[i - 1]] + 1);
            }
        }
    }

    ll n_odd = odd.size();
    // vector<vector<ll>> dp_odd(n_odd + 1, vector<ll>(m + 10, INF));
    vector<ll> dp_odd(m + 10, INF);
    // dp[i][j]<-i-1番目までの正四面体の取り方がわかっている時に、i番目の正四面体をいくつか取って合計数をjとする時の取った数の最小値
    // ナップザックdp 遷移はとるか撮らないか

    // dp_odd[0][0] = 0;
    dp_odd[0] = 0;
    rep_s(i, 1, n_odd + 1) {
        rep(j, m + 1) {
            // // 使わない場合
            // chmin(dp_odd[i][j], dp_odd[i - 1][j]);

            // // 横に展開
            // if (j - odd[i - 1] >= 0) {
            //     chmin(dp_odd[i][j], dp_odd[i][j - odd[i - 1]] + 1);
            // }

            if (j - odd[i - 1] >= 0) {
                chmin(dp_odd[j], dp_odd[j - odd[i - 1]] + 1);
            }
        }
    }

    while (1) {
        ll x;
        cin >> x;
        if (x == 0) return 0;
        cout << dp_both[x] << ' ' << dp_odd[x] << "\n";
        // cout << dp_both[n][x] << ' ' << dp_odd[n_odd][x] << "\n";
    }

    return 0;
}