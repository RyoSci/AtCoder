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
    Int h, w;
    cin >> h >> w;
    vector<vector<char>> s(h, vector<char>(w));
    Int black = 0;
    rep(i, h) {
        rep(j, w) {
            cin >> s[i][j];
            if (s[i][j] == '#') black++;
        }
    }

    vector<vector<Int>> dis(h, vector<Int>(w, INF));
    dis[0][0] = 1;
    queue<P> q;
    q.push(make_pair(0, 0));

    vector<Int> dx{-1, 0, 1, 0};
    vector<Int> dy{0, 1, 0, -1};

    while (!q.empty()) {
        Int x = q.front().first;
        Int y = q.front().second;
        q.pop();
        rep(i, 4) {
            Int nx = x + dx[i];
            Int ny = y + dy[i];
            if (0 <= nx && nx < h && 0 <= ny && ny < w && s[nx][ny] == '.' &&
                dis[nx][ny] > dis[x][y] + 1) {
                dis[nx][ny] = dis[x][y] + 1;
                q.push(make_pair(nx, ny));
            }
        }
    }
    if (dis[h - 1][w - 1] == INF)
        cout << -1 << "\n";
    else
        cout << h * w - black - dis[h - 1][w - 1] << "\n";
    return 0;
}