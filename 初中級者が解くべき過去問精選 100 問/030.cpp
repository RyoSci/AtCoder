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
vector<Int> dx{-1, 0, 1, 0};
vector<Int> dy{0, 1, 0, -1};

int main() {
    Int h, w, n;
    cin >> h >> w >> n;
    vector<P> start(n + 1);
    vector<P> goal(n + 1);
    vector<vector<char>> grid(h, vector<char>(w));

    rep(i, h) {
        rep(j, w) {
            cin >> grid[i][j];
            if (grid[i][j] == 'S') {
                start[0] = make_pair(i, j);
            } else if (grid[i][j] != '.' && grid[i][j] != 'X') {
                Int now = grid[i][j] - '0';
                // cout << now << "\n";
                goal[now - 1] = make_pair(i, j);
                start[now] = make_pair(i, j);
            }
        }
    }

    Int ans = 0;
    rep(i, n) {
        vector<vector<Int>> dis(h, vector<Int>(w, INF));
        queue<P> q;
        Int x = start[i].first;
        Int y = start[i].second;
        q.push(start[i]);
        dis[x][y] = 0;
        while (!q.empty()) {
            P now = q.front();
            q.pop();
            Int x = now.first;
            Int y = now.second;
            rep(i, 4) {
                Int nx = x + dx[i];
                Int ny = y + dy[i];
                if (0 <= nx && nx < h && 0 <= ny && ny < w &&
                    grid[nx][ny] != 'X') {
                    if (dis[nx][ny] > dis[x][y] + 1) {
                        dis[nx][ny] = dis[x][y] + 1;
                        q.push(make_pair(nx, ny));
                    }
                }
            }
        }
        ans += dis[goal[i].first][goal[i].second];
    }
    cout << ans << "\n";

    return 0;
}