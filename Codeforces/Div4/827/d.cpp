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
using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];

        vector<vector<ll>> ele(1001);
        rep(i, n) {
            ll m = a[i];
            for (ll j = 2; j * j <= a[i]; j++) {
                bool flag = false;
                while (m % j == 0) {
                    m /= j;
                    flag = true;
                }
                if (flag) ele[j].emplace_back(i);
            }
            if (m != 1) ele[m].emplace_back(i);
        }
        ll ans = 0;
        rep(i, n) {
            if (a[i] == 1) ans = max(ans, i + 1 + n);
        }

        rep_s(i, 2, 1001) {
            reverse(ele[i].begin(), ele[i].end());
            if (ele[i].size() > 0) {
                if (ele[i][0] == n - 1) {
                    ll flag = n;
                    rep(j, ele[i].size() - 1) {
                        if (ele[i][j] - 1 != ele[i][j + 1]) {
                            flag = ele[i][j] - 1;
                            break;
                        }
                    }
                    if (flag != n)
                        ans = max(ans, ele[i][0] + 1 + flag + 1);
                    else if (ele[i].back() != 0)
                        ans = max(ans, ele[i][0] + 1 + ele[i].back() - 1 + 1);
                } else
                    ans = max(ans, ele[i][0] + 1 + n);
            }
        }
        if (ans == 0)
            cout << -1 << "\n";
        else
            cout << ans << "\n";
    }
    return 0;
}