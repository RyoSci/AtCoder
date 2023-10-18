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

void chmin(ll &x, ll y) {
    if (x > y) x = y;
    return;
}
void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    ll h, w;
    cin >> h >> w;
    vector<string> a(h);
    for (ll i = 0; i < h; i++) cin >> a[i];

    vector dp(h, vector(w, 0ll));
    rep(i, h) rep(j, w) {
        if ((i + j) % 2 == 0)
            dp[i][j] = -INF;
        else
            dp[i][j] = INF;
    }

    vector<ll> di = {1, 0};
    vector<ll> dj = {0, 1};

    auto inner = [&](ll ni, ll nj) {
        if (0 <= ni and ni < h and 0 <= nj and nj < w)
            return true;
        else
            return false;
    };

    dp[h - 1][w - 1] = 0;
    rep_r(i, h - 1, -1) rep_r(j, w - 1, -1) {
        if ((i + j) % 2 == 0) {
            // 最大化したい
            rep(k, 2) {
                ll ni = i + di[k];
                ll nj = j + dj[k];
                if (inner(ni, nj)) {
                    if (a[ni][nj] == '+')
                        chmax(dp[i][j], dp[ni][nj] + 1);
                    else
                        chmax(dp[i][j], dp[ni][nj] - 1);
                }
            }
        } else {
            // 最小化したい
            rep(k, 2) {
                ll ni = i + di[k];
                ll nj = j + dj[k];
                if (inner(ni, nj)) {
                    if (a[ni][nj] == '+')
                        chmin(dp[i][j], dp[ni][nj] - 1);
                    else
                        chmin(dp[i][j], dp[ni][nj] + 1);
                }
            }
        }
    }

    if (dp[0][0] == 0)
        cout << "Draw"
             << "\n ";
    else {
        cout << (dp[0][0] > 0 ? "Takahashi" : "Aoki") << "\n";
    }
    return 0;
}