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

int main() {
    Int w, h;
    cin >> w >> h;
    vector<vector<Int>> grid(h, vector<Int>(w));
    rep(i, h) {
        rep(j, w) { cin >> grid[i][j]; }
    }

    vector<vector<Int>> inner(h, vector<Int>(w, -1));

    vector<Int> dx{-1, 0, 1, 1, 0, -1};
    vector<Int> dy1{0, 1, 0, -1, -1, -1};
    vector<Int> dy2{1, 1, 1, 0, -1, 0};

    // 内側の建物がない箇所を探す
    rep(i, h) {
        rep(j, w) {
            if (grid[i][j] == 0 && inner[i][j] == -1) {
                queue<P> q;
                q.push(make_pair(i, j));
                inner[i][j] = 1;
                bool flag = false;
                vector<P> tmp;
                tmp.push_back(make_pair(i, j));
                while (!q.empty()) {
                    Int x = q.front().first;
                    Int y = q.front().second;
                    q.pop();
                    rep(k, 6) {
                        Int nx = x + dx[k];
                        Int ny;
                        if (x % 2 == 0)
                            ny = y + dy2[k];
                        else
                            ny = y + dy1[k];
                        if (0 <= nx && nx < h && 0 <= ny && ny < w) {
                            if (grid[nx][ny] == 0 && inner[nx][ny] == -1) {
                                inner[nx][ny] = 1;
                                q.push(make_pair(nx, ny));
                                tmp.push_back(make_pair(nx, ny));
                            }
                        } else {
                            flag = true;
                        }
                    }
                }
                if (flag) {
                    rep_e(p, tmp) { inner[p.first][p.second] = 0; }
                }
            }
        }
    }

    // 各ますを探索して、隣が内側の何もないますであれば無視する。
    Int ans = 0;
    rep(i, h) {
        rep(j, w) {
            if (grid[i][j] == 1) {
                rep(k, 6) {
                    Int ni = i + dx[k];
                    Int nj;
                    if (i % 2 == 0) {
                        nj = j + dy2[k];
                    } else {
                        nj = j + dy1[k];
                    }
                    if (0 <= ni && ni < h && 0 <= nj && nj < w) {
                        if (grid[ni][nj] == 0 && inner[ni][nj] == 0) ans++;
                    } else {
                        ans++;
                    }
                }
            }
        }
    }
    cout << ans << "\n";
    return 0;
}