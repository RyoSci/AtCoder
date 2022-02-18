#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <stack>
using namespace std;
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
// typedef pair<Int, Int> P;
typedef pair<int, int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (int i = 0; i < n; i++)
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)

int main()
{
    int r1, c1;
    cin >> r1 >> c1;
    int r2, c2;
    cin >> r2 >> c2;

    vector<P> dxdy;
    rep(i, 4)
    {
        rep(j, 4)
        {
            if (i == 0 && j == 0 | i + j > 3)
            {
                /* code */
                continue;
            }
            dxdy.push_back(P(i, j));
            dxdy.push_back(P(i, -j));
            dxdy.push_back(P(-i, j));
            dxdy.push_back(P(-i, -j));
        }
    }

    bool flag = false;
    for (auto p : dxdy)
    {
        int nx, ny;
        nx = r1 + p.first;
        ny = c1 + p.second;
        if (nx + ny == r2 + c2 | nx - ny == r2 - c2 | abs(nx - r2) + abs(ny - c2) <= 3)
        {
            flag = true;
        }
    }

    int ans = 3;
    if (r1 == r2 && c1 == c2)
    {
        ans = 0;
    }
    else if (r1 + c1 == r2 + c2 | r1 - c1 == r2 - c2 | abs(r1 - r2) + abs(c1 - c2) <= 3)
    {
        /* code */
        ans = 1;
    }
    else if ((r1 + c1) % 2 == 0 && (r2 + c2) % 2 == 0)
    {
        /* code */
        ans = 2;
    }
    else if (flag)
    {
        /* code */
        ans = 2;
    }

    cout << ans << "\n";
    return 0;
}