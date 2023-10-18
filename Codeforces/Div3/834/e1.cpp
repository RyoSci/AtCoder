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

        vector dp(3, vector(2, 0ll));

        // 二次元だとa[i]を重複して足してしまうので不適
        dp[0][0] = h;
        rep(i, n) {
            rep(j, 3) {
                rep(k, 2) {
                    rep(l, 3) {
                        rep(m, 2) {
                            if (j + l < 3 and k + m < 2 and
                                a[i] < dp[j][k] * pow_ll(2, l) * pow_ll(3, m)) {
                                chmax(dp[j + l][k + m],
                                      dp[j][k] * pow_ll(2, l) * pow_ll(3, m) +
                                          a[i] / 2);
                            }
                        }
                    }
                }
            }
        }

        set<ll> ans;

        rep(j, 3) {
            rep(k, 2) {
                rep_s(i, 1, n + 1) {
                    if (dp[j][k] > a[i - 1]) ans.insert(i);
                }
                cout << j << ' ' << k << ' ' << dp[j][k] << "\n";
            }
        }
        cout << ans.size() << "\n";
    }
    return 0;
}