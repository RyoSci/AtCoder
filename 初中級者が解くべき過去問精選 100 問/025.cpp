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

Int w, h;
Int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
Int dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

vector<vector<Int>> c(50, vector<Int>(50));
Int nx, ny;

void dfs(Int x, Int y, vector<vector<Int>>& seen) {
    rep(i, 8) {
        nx = x + dx[i];
        ny = y + dy[i];
        if (0 <= nx && nx < h && 0 <= ny && ny < w) {
            if (c[nx][ny] == 1 && seen[nx][ny] == 0) {
                seen[nx][ny] = 1;
                dfs(nx, ny, seen);
            }
        }
    }
}

int main() {
    Int ans = 0;

    while (1) {
        cin >> w >> h;
        if (w == 0 && h == 0) break;
        vector<vector<Int>> seen(50, vector<Int>(50));
        // seen.resize(h, vector<Int>(w));
        // c.resize(h, vector<Int>(w));

        rep(i, h) {
            rep(j, w) { cin >> c[i][j]; }
        }
        ans = 0;
        rep(i, h) {
            rep(j, w) {
                if (c[i][j] == 0 || seen[i][j]) continue;
                seen[i][j] = 1;
                dfs(i, j, seen);
                ans++;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}