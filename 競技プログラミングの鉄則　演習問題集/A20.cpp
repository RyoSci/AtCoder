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

void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    string s;
    cin >> s;
    string t;
    cin >> t;
    ll n = s.size(), m = t.size();
    vector dp(n + 1, vector(m + 1, 0ll));

    rep_s(i, 1, n + 1) {
        rep_s(j, 1, m + 1) {
            chmax(dp[i][j], dp[i - 1][j]);
            chmax(dp[i][j], dp[i][j - 1]);
            if (s[i - 1] == t[j - 1]) chmax(dp[i][j], dp[i - 1][j - 1] + 1);
        }
    }

    cout << dp[n][m] << "\n";
    return 0;
}