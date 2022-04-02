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
    vector<vector<ll>> dp(n + 1, vector<ll>(200, 0));
    // dp[i][j]:=aからi個使う時に総和がjとなる数

    dp[0][0] = 1;
    rep(i, n) {
        rep(j, 200) {
            if (dp[i][j] == 0) continue;
            ll tmp = dp[i][j];
            // 使う場合
            dp[i + 1][(j + a[i]) % 200] += dp[i][j];
            if (dp[i + 1][(j + a[i]) % 200] < 0)
                dp[i + 1][(j + a[i]) % 200] = INF;
            // 使わない場合
            dp[i + 1][j] += dp[i][j];
            if (dp[i + 1][j] < 0) dp[i + 1][j] = INF;
        }
    }
    ll nj = -1;
    rep(j, 200) {
        if (j == 0 && dp[n][j] >= 3) {
            nj = j;
        } else if (j != 0 && dp[n][j] >= 2) {
            nj = j;
        }
    }
    if (nj == -1)
        cout << "No"
             << "\n";
    else {
        cout << "Yes"
             << "\n";
        vector<ll> b, c;
        // 使う方優先
        ll j = nj;
        rep_r(i, n, 0) {
            ll tmp = j;
            tmp -= a[i - 1];
            tmp %= 200;
            if (tmp < 0) tmp += 200;
            if (dp[i - 1][tmp] > 0) {
                j = tmp;
                b.push_back(i);
            } else {
                continue;
            }
        }

        j = nj;
        // 使わない方優先
        rep_r(i, n, 0) {
            ll tmp = j;
            tmp -= a[i - 1];
            tmp %= 200;
            if (tmp < 0) tmp += 200;
            if (tmp == j && j == 0 && c.size() == 0) {
                c.push_back(i);
                break;
            } else if (dp[i - 1][j] > 0) {
                continue;
            } else {
                j -= a[i - 1];
                j %= 200;
                if (j < 0) j += 200;
                c.push_back(i);
            }
        }

        reverse(b.begin(), b.end());
        reverse(c.begin(), c.end());

        cout << b.size() << " ";
        for (auto a : b) cout << a << " ";
        cout << endl;
        cout << c.size() << " ";
        for (auto a : c) cout << a << " ";
        cout << endl;
    }

    // for (auto a : dp[n]) cout << a << " ";
    // cout << endl;

    return 0;
}