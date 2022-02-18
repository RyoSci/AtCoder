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
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG
// #include <atcoder/all>
// #include <atcoder/modint>
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;

void chmin(ll& x, ll y) {
    if (x > y) x = y;
    return;
}

int main() {
    ll n;
    cin >> n;
    vector<vector<char>> s(5, vector<char>(n));
    rep(i, 5) {
        rep(j, n) { cin >> s[i][j]; }
    }

    vector<vector<ll>> dp(n, vector<ll>(3, INF));

    // dp[i][j]<-i-1番目までの列を色の塗り方が決まっている場合に、i番目の列をjの色で塗りつぶす際のそれまでに塗りつぶしてきたマスの最小値
    // 答えは最後の列の各色の塗り方の通り数のminをとる
    // 同じ色を２連続で使ってはいけないのでi番目の色からi+1番目に使用できる色はそれ以外の二色
    // R:0, B:1, W:2

    vector<char> color{'R', 'B', 'W'};
    rep(i, 3) {
        ll cnt = 0;
        rep(l, 5) {
            if (s[l][0] != color[i]) cnt++;
        }
        chmin(dp[0][i], cnt);
    }

    rep_s(i, 1, n) {
        rep(j, 3) {
            rep(k, 3) {
                if (j == k) continue;
                ll cnt = 0;
                rep(l, 5) {
                    if (s[l][i] != color[k]) cnt++;
                }
                chmin(dp[i][k], dp[i - 1][j] + cnt);
            }
        }
    }

    ll ans = INF;
    rep(i, 3) { ans = min(ans, dp[n - 1][i]); }
    cout << ans << "\n";
    return 0;
}