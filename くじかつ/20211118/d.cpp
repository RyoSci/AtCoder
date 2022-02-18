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
    int h, w;
    cin >> h >> w;
    vector<string> s(h);
    rep(i, h)
    {
        cin >> s[i];
    }
    vector<vector<int>> dp(h, vector<int>(w, INF));
    dp[0][0] = 0;
    rep(i, h)
    {
        rep(j, w)
        {
            if (i + 1 < h)
            {
                /* code */
                if (s[i + 1][j] == s[i][j])
                {
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j]);
                }
                else
                {
                    /* code */
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1);
                }
            }
            if (j + 1 < w)
            {
                /* code */
                if (s[i][j + 1] == s[i][j])
                {
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j]);
                }
                else
                {
                    /* code */
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1);
                }
            }
        }
    }
    if (s[0][0] == '.' && s[h - 1][w - 1] == '.')
    {
        /* code */
        cout << dp[h - 1][w - 1] / 2 << "\n";
    }
    else if (s[0][0] == '#' && s[h - 1][w - 1] == '#')
    {

        /* code */
        cout << dp[h - 1][w - 1] / 2 + 1 << "\n";
    }
    else
    {
        cout << (dp[h - 1][w - 1] + 1) / 2 << "\n";
    }

    return 0;
}