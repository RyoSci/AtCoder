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
    Int r, c;
    cin >> r >> c;
    Int sy, sx;
    cin >> sy >> sx;
    --sy;
    --sx;
    Int gy, gx;
    cin >> gy >> gx;
    --gy;
    --gx;
    vector<vector<char>> a(r, vector<char>(c));
    rep(i, r) {
        rep(j, c) { cin >> a[i][j]; }
    }

    vector<vector<Int>> dis(r, vector<Int>(c, INF));
    dis[sy][sx] = 0;
    queue<P> q;
    q.push(make_pair(sy, sx));

    vector<Int> dx{0, 1, 0, -1};
    vector<Int> dy{-1, 0, 1, 0};

    while (!q.empty()) {
        P now = q.front();
        q.pop();
        Int y = now.first;
        Int x = now.second;
        rep(i, 4) {
            Int ny = y + dy[i];
            Int nx = x + dx[i];
            if (0 <= nx && nx < c && 0 <= ny && ny < r && a[ny][nx] == '.') {
                if (dis[ny][nx] > dis[y][x] + 1) {
                    dis[ny][nx] = dis[y][x] + 1;
                    q.push(make_pair(ny, nx));
                }
            }
        }
    }

    cout << dis[gy][gx] << "\n";
    return 0;
}