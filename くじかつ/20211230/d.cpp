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

int main() {
    Int h, w;
    cin >> h >> w;
    vector<string> s(h);
    rep(i, h) { cin >> s[i]; }

    vector<Int> dx = {0, 1, 0, -1};
    vector<Int> dy = {1, 0, -1, 0};
    Int ans = 0;
    rep(i, h) {
        rep(j, w) {
            if (s[i][j] == '#') continue;

            vector<vector<Int>> dis(h, vector<Int>(w, -1));
            dis[i][j] = 0;

            queue<P> q;
            q.push(P(i, j));

            while (!q.empty()) {
                P par = q.front();
                q.pop();
                Int x = par.first;
                Int y = par.second;
                rep(k, 4) {
                    Int nx = x + dx[k];
                    Int ny = y + dy[k];
                    if (0 <= nx && nx < h && 0 <= ny && ny < w &&
                        s[nx][ny] == '.') {
                        if (dis[nx][ny] == -1) {
                            dis[nx][ny] = dis[x][y] + 1;
                            q.push(P(nx, ny));
                        }
                    }
                }
                Int tmp = 0;
                rep(ii, h) {
                    rep(jj, w) { tmp = max(tmp, dis[ii][jj]); }
                }
                ans = max(ans, tmp);
            }
        }
    }
    cout << ans << "\n";
    return 0;
}