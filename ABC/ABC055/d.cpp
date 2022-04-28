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

ll n;
string s;
vector<ll> dp;

bool f(ll i) {
    bool ans = false;
    if (dp[i] == 0) {
        if (s[i] == 'o') {
            if (dp[(i - 1 + n) % n] == dp[(i + 1) % n] ^ 1) ans = true;
        } else if (dp[(i - 1 + n) % n] == dp[(i + 1) % n])
            ans = true;
    } else {
        if (s[i] == 'o') {
            if (dp[(i - 1 + n) % n] == dp[(i + 1) % n]) ans = true;
        } else if (dp[(i - 1 + n) % n] == dp[(i + 1) % n] ^ 1)
            ans = true;
    }
    return ans;
}

int main() {
    cin >> n;
    cin >> s;
    // 0が狼、1が羊
    dp.resize(n, -1);

    rep(i, 1 << 2) {
        rep(j, 2) dp[j] = i >> j & 1;
        rep_s(j, 1, n - 1) {
            if (dp[j] == 0) {
                if (s[j] == 'o')
                    dp[j + 1] = dp[j - 1] ^ 1;
                else
                    dp[j + 1] = dp[j - 1];
            } else {
                if (s[j] == 'o')
                    dp[j + 1] = dp[j - 1];
                else
                    dp[j + 1] = dp[j - 1] ^ 1;
            }
        }

        string WS = "WS";

        if (f(n - 1) && f(0)) {
            for (auto a : dp) cout << WS[a] << "";
            cout << endl;
            return 0;
        }
    }

    cout << -1 << "\n";
    return 0;
}