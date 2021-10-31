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

string ans = "Nothing";
vector<vector<int>> t(5, vector<int>(5));
void dfs(int n, int k, int res)
{
    if (n == 0)
    {
        if (res == 0)
        {
            /* code */
            ans = "Found";
        }
        return;
    }
    rep(i, k)
    {
        dfs(n - 1, k, res ^ t[n - 1][i]);
    }
    return;
}

int main()
{
    int n, k;
    cin >> n >> k;
    rep(i, n)
    {
        rep(j, k)
        {
            cin >> t[i][j];
        }
    }
    dfs(n, k, 0);
    cout << ans << "\n";

    return 0;
}