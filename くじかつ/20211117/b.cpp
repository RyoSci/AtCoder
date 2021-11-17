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
#include <iomanip>
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
    int h, w, x, y;
    cin >> h >> w >> x >> y;
    vector<string> s(h);
    rep(i, h)
    {
        cin >> s[i];
    }
    int res = 0;
    rep_s(i, x - 1, h)
    {
        if (s[i][y - 1] == '.')
        {
            /* code */
            res++;
        }
        else
        {
            /* code */
            break;
        }
    }
    rep_r(i, x - 1, -1)
    {
        if (s[i][y - 1] == '.')
        {
            /* code */
            res++;
        }
        else
        {
            /* code */
            break;
        }
    }
    rep_s(i, y - 1, w)
    {
        if (s[x - 1][i] == '.')
        {
            /* code */
            res++;
        }
        else
        {
            /* code */
            break;
        }
    }
    rep_r(i, y - 1, -1)
    {
        if (s[x - 1][i] == '.')
        {
            /* code */
            res++;
        }
        else
        {
            /* code */
            break;
        }
    }
    cout << res - 3 << "\n";
    return 0;
}