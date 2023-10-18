// #define _GLIBCXX_DEBUG
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
// #define MOD 1000000007
#define MOD 998244353
#define INF (1LL << 60)
#define EPS (1e-10)
using namespace std;
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

ll pow_ll(ll n, ll p) {
    ll rest = 1;
    while (p) {
        if (p % 2 == 1) rest *= n;
        n *= n;
        p >>= 1;
    }
    return rest;
}

int main() {
    ll t;
    cin >> t;
    rep(_, t) {
        ll n, h;
        cin >> n >> h;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        sort(a.begin(), a.end());

        // vector<vector<vector<ll>>> dp(n + 1,
        //                               vector<vector<ll>>(3, vector<ll>(2,
        //                               0)));
        vector dp(n + 1, vector(3, vector(2, 0ll)));

        dp[0][0][0] = h;
        rep(i, n) {
            rep(j, 3) {
                rep(k, 2) {
                    rep(l, 3) {
                        rep(m, 2) {
                            if (j + l < 3 and k + m < 2 and
                                a[i] <
                                    dp[i][j][k] * pow_ll(2, l) * pow_ll(3, m)) {
                                chmax(
                                    dp[i + 1][j + l][k + m],
                                    dp[i][j][k] * pow_ll(2, l) * pow_ll(3, m) +
                                        a[i] / 2);
                            }
                        }
                    }

                    // // 真に大
                    // if (a[i] < dp[i][j][k])
                    //     chmax(dp[i + 1][j][k], dp[i][j][k] + a[i] / 2);
                    // // 2倍使う
                    // if (j < 2 and a[i] < dp[i][j][k] * 2) {
                    //     chmax(dp[i + 1][j + 1][k], dp[i][j][k] * 2 + a[i] /
                    //     2);
                    // }
                    // // 3倍使う
                    // if (k == 0 and a[i] < dp[i][j][k] * 3) {
                    //     chmax(dp[i + 1][j][k + 1], dp[i][j][k] * 3 + a[i] /
                    //     2);
                    // }
                    // // 4倍使う
                    // if (j == 0 and a[i] < dp[i][j][k] * 4) {
                    //     chmax(dp[i + 1][j + 2][k], dp[i][j][k] * 4 + a[i] /
                    //     2);
                    // }
                    // // 6倍使う
                    // if (j < 2 and k == 0 and a[i] < dp[i][j][k] * 6) {
                    //     chmax(dp[i + 1][j + 1][k + 1],
                    //           dp[i][j][k] * 6 + a[i] / 2);
                    // }
                    // // 12倍使う
                    // if (j == 0 and k == 0 and a[i] < dp[i][j][k] * 12) {
                    //     chmax(dp[i + 1][j + 2][k + 1],
                    //           dp[i][j][k] * 12 + a[i] / 2);
                }
            }
        }

        set<ll> ans;

        rep_s(i, 1, n + 1) {
            rep(j, 3) {
                rep(k, 2) {
                    if (dp[i][j][k] > a[i - 1]) ans.insert(i);
                    // cout << i << ' ' << j << ' ' << k << ' ' << dp[i][j][k]
                    //      << "\n";
                }
            }
        }
        cout << ans.size() << "\n";
    }
    return 0;
}