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

void chmax(ll &x, ll y) {
    if (x < y) x = y;
}

int main() {
    ll n;
    cin >> n;
    vector<ll> p(n), a(n);
    rep(i, n) cin >> p[i] >> a[i];
    vector dp(n + 2, vector(n + 2, 0ll));
    queue<P> q;
    q.emplace(P(0, n + 1));

    vector seen(n + 2, vector(n + 2, false));

    while (q.size()) {
        auto [l, r] = q.front();
        q.pop();
        if (seen[l][r]) continue;
        seen[l][r] = true;

        // 左端を取る
        if (l + 1 < r) {
            ll nx = 0;
            if (p[l + 1 - 1] > l and r > p[l + 1 - 1]) {
                nx = a[l + 1 - 1];
            }
            chmax(dp[l + 1][r], dp[l][r] + nx);
            q.emplace(P(l + 1, r));
        }
        // 右端を取る
        if (l + 1 < r) {
            ll nx = 0;
            if (p[r - 1 - 1] > l and r > p[r - 1 - 1]) {
                nx = a[r - 1 - 1];
            }
            chmax(dp[l][r - 1], dp[l][r] + nx);
            q.emplace(P(l, r - 1));
        }
    }

    ll ans = 0;
    rep(i, n + 1) chmax(ans, dp[i][i + 1]);
    cout << ans << "\n";
    return 0;
}