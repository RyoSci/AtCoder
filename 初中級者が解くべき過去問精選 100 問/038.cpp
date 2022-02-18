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

void chmax(ll &x, ll y) {
    if (y > x) x = y;
    return;
}

int main() {
    ll q;
    cin >> q;
    rep(i, q) {
        string s, t;
        cin >> s >> t;
        ll n, m;
        n = s.length();
        m = t.length();
        vector<vector<ll>> dp(n + 1, vector<ll>(m + 1));

        // dp[i][j]<-sのi番目までの文字を見た時に、tのj番目の文字まででの一致数の最大値
        rep(i, n) {
            rep_s(j, 1, m + 1) {
                chmax(dp[i + 1][j], dp[i][j]);
                chmax(dp[i + 1][j], dp[i + 1][j - 1]);
                // 一致した場合
                if (s[i] == t[j - 1]) {
                    chmax(dp[i + 1][j], dp[i][j - 1] + 1);
                }
            }
        }
        cout << dp[n][m] << "\n";
    }
    return 0;
}