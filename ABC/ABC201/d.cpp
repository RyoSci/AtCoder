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

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}
void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    ll h, w;
    cin >> h >> w;
    vector<string> a(h);

    rep(i, h) cin >> a[i];

    vector<vector<ll>> dp(h, vector<ll>(w, -INF));

    // dp[i][j]:=i,jにいる時のTーAの最大スコア。Tは最大になるように、Aは最小になるように動く

    dp[h - 1][w - 1] = 0;

    rep_r(i, h - 1, -1) {
        rep_r(j, w - 1, -1) {
            if (i + 1 < h) {
                ll b = a[i + 1][j] == '-' ? -1 : 1;
                chmax(dp[i][j], b - dp[i + 1][j]);
            }

            if (j + 1 < w) {
                ll c = a[i][j + 1] == '-' ? -1 : 1;
                chmax(dp[i][j], c - dp[i][j + 1]);
            }
        }
    }

    // rep(i, h) {
    //     for (auto a : dp[i]) cout << a << " ";
    //     cout << endl;
    // }

    if (dp[0][0] == 0)
        cout << "Draw"
             << "\n";
    else if (dp[0][0] > 0)
        cout << "Takahashi"
             << "\n";
    else
        cout << "Aoki"
             << "\n";
    return 0;
}