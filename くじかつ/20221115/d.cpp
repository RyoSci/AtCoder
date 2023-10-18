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
#define INF (1L << 60)
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
    ll n, s;
    cin >> n >> s;
    vector<ll> a(n), b(n);
    rep(i, n) cin >> a[i] >> b[i];

    vector<vector<ll>> dp(n + 1, vector<ll>(s + 1, 0));
    dp[0][0] = 1;
    rep(i, n) {
        rep(j, s + 1) {
            if (dp[i][j] == 0) continue;
            ll nj = j + a[i];
            if (nj <= s) dp[i + 1][nj] = dp[i][j];
            nj = j + b[i];
            if (nj <= s) dp[i + 1][nj] = dp[i][j];
        }
    }

    if (dp[n][s] == 1) {
        cout << "Yes"
             << "\n";
        ll now = s;
        vector<char> ans;

        rep_r(i, n - 1, -1) {
            ll nx = now - a[i];
            if (0 <= nx and dp[i][nx] == 1) {
                now = nx;
                ans.emplace_back('H');
                continue;
            }
            nx = now - b[i];
            if (0 <= nx and dp[i][nx] == 1) {
                now = nx;
                ans.emplace_back('T');
                continue;
            }
        }
        reverse(ans.begin(), ans.end());
        for (auto a : ans) cout << a << "";
        cout << endl;
    } else {
        cout << "No"
             << "\n";
    }
    return 0;
}