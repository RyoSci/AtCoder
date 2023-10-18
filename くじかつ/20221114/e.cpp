#define _GLIBCXX_DEBUG
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

void chmin(double &x, double y) {
    if (x > y) x = y;
    return;
}

double dis(double x1, double x2, double y1, double y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> x(n + m + 1), y(n + m + 1);
    rep(i, n) cin >> x[i + 1] >> y[i + 1];
    vector<ll> p(m), q(m);
    rep(i, m) cin >> p[i] >> q[i];

    rep_s(i, n + 1, n + m + 1) {
        x[i] = p[i - n - 1];
        y[i] = q[i - n - 1];
    }

    vector<vector<double>> dp(1 << (n + m + 1),
                              vector<double>((n + m + 1), INF));
    dp[1][0] = 0;

    rep(i, 1 << (n + m + 1)) {
        double bs = 1.0;
        rep_s(j, n + 1, n + m + 1) {
            if (i >> j & 1) bs *= 2.0;
        }

        rep(j, n + m + 1) {
            if (!(i >> j & 1)) continue;
            rep(k, n + m + 1) {
                chmin(dp[i | (1 << k)][k],
                      dp[i][j] + dis(x[j], x[k], y[j], y[k]) / bs);
            }
        }
    }

    double ans = INF;
    ll mask = (1 << (n + 1)) - 1;
    rep(i, 1 << m) {
        double bs = 1.0;
        rep(j, m) {
            if (i >> j & 1) bs *= 2.0;
        }
        ll ni = i << (n + 1);
        ll nmask = mask | ni;
        rep(j, n + m + 1) {
            chmin(ans, dp[nmask][j] + dis(x[j], x[0], y[j], y[0]) / bs);
        }
    }
    //小数点以下の長さを指定
    cout << fixed << setprecision(15) << ans << endl;
    return 0;
}