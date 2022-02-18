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

Int h, w;
bool check(Int x, Int y) { return 0 <= x && x < h && 0 <= y && y < w; }

int main() {
    while (1) {
        cin >> w >> h;
        if (h == 0 && w == 0) return 0;
        vector<vector<Int>> tate(h - 1, vector<Int>(w));
        vector<vector<Int>> yoko(h, vector<Int>(w - 1));
        rep(i, h - 1) {
            rep(j, w - 1) { cin >> yoko[i][j]; }
            rep(j, w) { cin >> tate[i][j]; }
        }
        rep(j, w - 1) { cin >> yoko[h - 1][j]; }

        vector<vector<Int>> dis(h, vector<Int>(w, INF));

        queue<P> q;
        q.push(make_pair(0, 0));
        dis[0][0] = 1;

        while (!q.empty()) {
            Int x = q.front().first;
            Int y = q.front().second;
            q.pop();
            Int nx, ny;
            // 上
            nx = x - 1;
            ny = y;
            if (check(nx, ny)) {
                if (tate[x - 1][y] == 0 && dis[nx][ny] > dis[x][y] + 1) {
                    dis[nx][ny] = dis[x][y] + 1;
                    q.push(make_pair(nx, ny));
                }
            }
            // 下
            nx = x + 1;
            ny = y;
            if (check(nx, ny)) {
                if (tate[x][y] == 0 && dis[nx][ny] > dis[x][y] + 1) {
                    dis[nx][ny] = dis[x][y] + 1;
                    q.push(make_pair(nx, ny));
                }
            }
            // 右
            nx = x;
            ny = y + 1;
            if (check(nx, ny)) {
                if (yoko[x][y] == 0 && dis[nx][ny] > dis[x][y] + 1) {
                    dis[nx][ny] = dis[x][y] + 1;
                    q.push(make_pair(nx, ny));
                }
            }
            // 左
            nx = x;
            ny = y - 1;
            if (check(nx, ny)) {
                if (yoko[x][y - 1] == 0 && dis[nx][ny] > dis[x][y] + 1) {
                    dis[nx][ny] = dis[x][y] + 1;
                    q.push(make_pair(nx, ny));
                }
            }
        }
        if (dis[h - 1][w - 1] == INF)
            cout << 0 << "\n";
        else
            cout << dis[h - 1][w - 1] << "\n";
    }
    return 0;
}