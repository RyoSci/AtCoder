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
using namespace std;
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (Int i = 0; i < n; i++)
#define rep_r(i, k, n) for (Int i = k; i > n; i--)
#define rep_s(i, k, n) for (Int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)
// #include <atcoder/all>
// #include <atcoder/modint>
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;

vector<vector<Int>> c(90, vector<Int>(90));
vector<Int> dx{-1, 0, 1, 0};
vector<Int> dy{0, 1, 0, -1};
vector<vector<Int>> seen(90, vector<Int>(90));

Int m, n;
Int ans = 0;

void dfs(Int x, Int y, Int px = -1, Int py = -1, Int cnt = 0) {
    seen[x][y] = 1;
    rep(i, 4) {
        Int nx = x + dx[i];
        Int ny = y + dy[i];
        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
            if (seen[nx][ny] == 1) continue;
            if (c[nx][ny] == 1) {
                // if (c[nx][ny] == 1 && !(nx == px && ny == py)) {
                dfs(nx, ny, x, y, cnt + 1);
            }
        }
    }
    ans = max(ans, cnt);
    seen[x][y] = 0;
}

int main() {
    cin >> m >> n;

    rep(i, n) {
        rep(j, m) { cin >> c[i][j]; }
    }

    // Int ans = 0;
    rep(i, n) {
        rep(j, m) {
            // ans = max(ans, dfs(i, j) + 1);
            dfs(i, j);
        }
    }
    cout << ans << "\n";
    return 0;
}