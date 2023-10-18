// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
#include <atcoder/modint>
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
using mint = modint1000000007;
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

vector<ll> di = {-1, 0, 1, 0};
vector<ll> dj = {0, 1, 0, -1};

int main() {
    ll h, w;
    cin >> h >> w;
    vector<vector<ll>> a(h, vector<ll>(w, 0));
    rep(i, h) rep(j, w) cin >> a[i][j];
    vector<vector<mint>> dp(h, vector<mint>(w, 1));

    priority_queue<tuple<ll, ll, ll>> q;
    rep(i, h) rep(j, w) { q.push(make_tuple(-a[i][j], i, j)); }

    while (!q.empty()) {
        auto [ai, i, j] = q.top();
        q.pop();
        rep(k, 4) {
            ll ni = i + di[k];
            ll nj = j + dj[k];
            if (0 <= ni && ni < h && 0 <= nj && nj < w) {
                if (a[ni][nj] > a[i][j]) dp[ni][nj] += dp[i][j];
            }
        }
    }

    mint ans = 0;
    rep(i, h) rep(j, w) { ans += dp[i][j]; }

    cout << ans.val() << "\n";
    return 0;
}