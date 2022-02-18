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
    Int mod = 998244353;
    Int n;
    cin >> n;
    vector<Int> a(n);
    for (Int i = 0; i < n; i++)
        cin >> a[i];
    vector<vector<Int>> dp(n, vector<Int>(10));
    dp[0][a[0]] = 1;
    for (Int i = 0; i < n - 1; i++)
    {
        for (Int j = 0; j < 10; j++)
        {
            if (dp[i][j] > 0)
            {
                Int tmp = j + a[i + 1];
                tmp %= 10;
                dp[i + 1][tmp] += dp[i][j];
                dp[i + 1][tmp] %= mod;
                tmp = j * a[i + 1];
                tmp %= 10;
                dp[i + 1][tmp] += dp[i][j];
                dp[i + 1][tmp] %= mod;
            }
        }
    }
    rep(i, 10)
    {
        cout << dp[n - 1][i] % mod << "\n";
    }
    return 0;
}