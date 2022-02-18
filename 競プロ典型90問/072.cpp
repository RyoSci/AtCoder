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
#define rep(i, n) for (int i = 0; i < n; i++)
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)

int ans = 0;
int h, w;
vector<int> dx = {0, 1, 0, -1};
vector<int> dy = {1, 0, -1, 0};
vector<string> c;

void dfs(int x, int y, vector<vector<int>> &seen, vector<vector<int>> &time) {
    seen[x][y] = 1;
    for (int i = 0; i < 4; i++) {
        int nx, ny;
        nx = x + dx[i];
        ny = y + dy[i];
        if (!(0 <= nx && nx < h && 0 <= ny && ny < w)) continue;
        if (c[nx][ny] == '#') continue;
        if (time[nx][ny] == -1) {
            time[nx][ny] = time[x][y] + 1;
            dfs(nx, ny, seen, time);
        } else {
            ans = max(ans, time[x][y] - time[nx][ny] + 1);
        }
    }
    time[x][y] = -1;
    return;
}

int main() {
    cin >> h >> w;
    c.resize(h);
    rep(i, h) { cin >> c[i]; }
    vector<vector<int>> seen(h, vector<int>(w, 0));
    vector<vector<int>> time(h, vector<int>(w, -1));
    rep(i, h) {
        rep(j, w) {
            if (seen[i][j] | c[i][j] == '#') continue;
            dfs(i, j, seen, time);
        }
    }

    if (ans <= 2)
        cout << -1 << "\n";
    else
        cout << ans << "\n";

    return 0;
}