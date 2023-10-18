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

int main() {
    ll a, b, c;
    cin >> a >> b >> c;
    ll n = 101;
    vector dp(n, vector(n, vector(n, 0.0)));

    rep_r(i, n - 2, -1) rep_r(j, n - 2, -1) rep_r(k, n - 2, -1) {
        dp[i][j][k] += (dp[i + 1][j][k] + 1.0) * double(i) / double(i + j + k);
        dp[i][j][k] += (dp[i][j + 1][k] + 1.0) * double(j) / double(i + j + k);
        dp[i][j][k] += (dp[i][j][k + 1] + 1.0) * double(k) / double(i + j + k);
    }
    // 小数点以下の長さを指定
    cout << fixed << setprecision(15) << dp[a][b][c] << endl;

    return 0;
}