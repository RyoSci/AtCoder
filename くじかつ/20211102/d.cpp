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
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (int i = 0; i < n; i++)
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)

int main()
{
    int sx, sy, tx, ty;
    cin >> sx >> sy >> tx >> ty;
    string res = "";

    // 1周目
    rep(i, tx - sx)
    {
        res += 'R';
    }
    rep(i, ty - sy)
    {
        res += 'U';
    }
    rep(i, tx - sx)
    {
        res += 'L';
    }
    rep(i, ty - sy)
    {
        res += 'D';
    }

    // 2周目
    res += 'D';
    rep(i, tx - sx)
    {
        res += 'R';
    }
    res += 'R';
    res += 'U';
    rep(i, ty - sy)
    {
        res += 'U';
    }
    res += 'L';
    res += 'U';
    rep(i, tx - sx)
    {
        res += 'L';
    }
    res += 'L';
    res += 'D';
    rep(i, ty - sy)
    {
        res += 'D';
    }
    res += 'R';

    cout << res << "\n";

    return 0;
}