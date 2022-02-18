#include <algorithm>
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
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)
// #include <atcoder/all>
// #include <atcoder/modint>
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;

int main() {
    ll n, k;
    cin >> n >> k;
    vector<vector<vector<ll>>> dp(n, vector<vector<ll>>(3, vector<ll>(2)));
    // dp[i][j][k]<-i-1番目までの予定が決まっている状態で、i番目のパスタソースをjにする時に、k回連続して使用した際の通り数。
    dp[0][0][0] = 1;
    dp[0][1][0] = 1;
    dp[0][2][0] = 1;
    rep(i, k) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        rep(j, 3) {
            if (j == b) continue;
            dp[a][j][0] = -1;
            dp[a][j][1] = -1;
        }
    }

    rep(i, n - 1) {
        rep(j, 3) {
            if (dp[i][j][0] == -1) continue;
            rep(k, 3) {
                if (dp[i + 1][k][0] == -1) continue;
                if (j == k)
                    dp[i + 1][k][1] = dp[i][j][0] % 10000;
                else {
                    dp[i + 1][k][0] += dp[i][j][0] + dp[i][j][1];
                    dp[i + 1][k][0] %= 10000;
                }
            }
        }
    }

    ll ans = 0;
    rep(i, 3) {
        rep(j, 2) {
            if (dp[n - 1][i][j] != -1) {
                ans += dp[n - 1][i][j];
                ans %= 10000;
            }
        }
    }
    cout << ans << "\n";

    // rep(i, n) {
    //     for (auto a : dp[i]) cout << a[0] << " " << a[1] << " ";
    //     cout << endl;
    // }
    return 0;
}