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

int main() {
    ll h, w, k;
    cin >> h >> w >> k;
    ll x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    x1--;
    y1--;
    x2--;
    y2--;
    vector<string> c(h);
    for (ll i = 0; i < h; i++) cin >> c[i];

    vector dp(h, vector(w, vector(2, INF)));

    dp[x1][y1][0] = 1;
    dp[x1][y1][1] = 1;

    priority_queue<tuple<ll, ll, ll, ll, ll>> pq;
    pq.emplace(-1, k, 0, x1, y1);
    pq.emplace(-1, k, 1, x1, y1);
    pq.emplace(-1, k, 2, x1, y1);
    pq.emplace(-1, k, 3, x1, y1);

    vector<ll> dx = {-1, 0, 1, 0};
    vector<ll> dy = {0, 1, 0, -1};

    while (pq.size()) {
        auto [cnt, rest, dir, i, j] = pq.top();
        pq.pop();
        cnt *= -1;

        // 同じ方向に進む
        ll ni, nj;
        ni = i + dx[dir];
        nj = j + dy[dir];

        if (0 <= ni and ni < h and 0 <= nj and nj < w and c[ni][nj] == '.') {
            if (dp[ni][nj][dir % 2] > cnt and
                dp[ni][nj][(dir % 2) ^ 1] >= cnt) {
                dp[ni][nj][dir % 2] = cnt;
                if (rest > 1)
                    pq.emplace(-cnt, rest - 1, dir, ni, nj);
                else {
                    pq.emplace(-(cnt + 1), k, 0, ni, nj);
                    pq.emplace(-(cnt + 1), k, 1, ni, nj);
                    pq.emplace(-(cnt + 1), k, 2, ni, nj);
                    pq.emplace(-(cnt + 1), k, 3, ni, nj);
                }
            }
        }

        vector<ll> tmp = {1, -1};

        // 向きを変える
        rep_e(add, tmp) {
            ll ndir;
            ndir = (dir + add + 4) % 4;
            ni = i + dx[ndir];
            nj = j + dy[ndir];
            if (0 <= ni and ni < h and 0 <= nj and nj < w and
                c[ni][nj] == '.') {
                if (dp[ni][nj][ndir % 2] > cnt + 1 and
                    dp[ni][nj][(ndir % 2) ^ 1] >= cnt + 1) {
                    dp[ni][nj][ndir % 2] = cnt + 1;
                    if (k > 1)
                        pq.emplace(-(cnt + 1), k - 1, ndir, ni, nj);
                    else {
                        pq.emplace(-(cnt + 2), k, 0, ni, nj);
                        pq.emplace(-(cnt + 2), k, 1, ni, nj);
                        pq.emplace(-(cnt + 2), k, 2, ni, nj);
                        pq.emplace(-(cnt + 2), k, 3, ni, nj);
                    }
                }
            }
        }
    }

    ll ans = min(dp[x2][y2][0], dp[x2][y2][1]);
    if (ans == INF) ans = -1;

    cout << ans << "\n";
    return 0;
}