// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
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
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

vector<vector<ll>> seen(16, vector<ll>(16, 0));
vector<ll> dx = {-1, 0, 1, 0};
vector<ll> dy = {0, 1, 0, -1};
ll h, w;
vector<string> c(16);
ll ans = 0;

void dfs(ll i, ll j, ll cnt, ll si, ll sj) {
    if (i == si and j == sj) {
        ans = max(ans, cnt);
    }
    rep(k, 4) {
        ll ni = i + dx[k];
        ll nj = j + dy[k];
        if (0 <= ni and ni < h and 0 <= nj and nj < w) {
            if (seen[ni][nj] == 0 and c[ni][nj] == '.') {
                seen[ni][nj] = 1;
                dfs(ni, nj, cnt + 1, si, sj);
                seen[ni][nj] = 0;
            }
        }
    }
}

int main() {
    cin >> h >> w;
    rep(i, h) cin >> c[i];

    rep(i, h) rep(j, w) {
        if (c[i][j] == '.') dfs(i, j, 0, i, j);
    }
    if (ans < 3)
        cout << -1 << "\n";
    else
        cout << ans << "\n";
    return 0;
}