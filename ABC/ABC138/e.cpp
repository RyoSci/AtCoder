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
    string s;
    cin >> s;
    string t;
    cin >> t;
    ll n, m;
    n = s.length();
    m = t.length();
    vector<vector<ll>> indexs(26);
    rep(i, n) {
        ll tmp = s.at(i) - 'a';
        indexs[tmp].push_back(i);
    }
    rep(i, 26) { indexs[i].push_back(INF); }

    ll ans = -1;
    // if (n == 1) {
    //     rep(i, m) {
    //         if (t.at(i) != s.at(0)) {
    //             ans = -1;
    //             cout << ans << "\n";
    //             return 0;
    //         }
    //     }
    //     ans = m;
    //     cout << ans << "\n";
    // } else {
    rep(i, m) {
        ll tmp = t.at(i) - 'a';
        if (indexs[tmp].size() == 1) {
            ans = -1;
            cout << ans << "\n";
            return 0;
        }
        auto iter =
            upper_bound(indexs[tmp].begin(), indexs[tmp].end(), ans % n);
        if (*iter == INF) {
            if (ans % n == 0) ans += n;
            ans = (ans + n - 1) / n * n;
            ans += indexs[tmp][0];
        } else {
            ans += *iter - ans % n;
        }
    }
    cout << ans + 1 << "\n";
    // }
    return 0;
}