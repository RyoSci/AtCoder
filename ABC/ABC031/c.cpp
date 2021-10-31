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
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    int ans = -INF;
    rep(i, n)
    {
        int res;
        int tmp;
        tmp = -INF;
        rep(j, n)
        {
            int taka, aoki;
            taka = 0;
            aoki = 0;
            if (i == j)
            {
                /* code */
                continue;
            }
            else if (i < j)
            {
                /* code */
                rep_s(k, i, j + 1)
                {
                    if ((k - i) % 2 == 0)
                    {
                        /* code */
                        taka += a[k];
                    }
                    else
                    {
                        aoki += a[k];
                    }
                }
            }
            else if (i > j)
            {
                /* code */
                rep_s(k, j, i + 1)
                {
                    if ((k - j) % 2 == 0)
                    {
                        /* code */
                        taka += a[k];
                    }
                    else
                    {
                        aoki += a[k];
                    }
                }
            }
            if (aoki > tmp)
            {
                /* code */
                tmp = aoki;
                res = taka;
            }
        }
        ans = max(ans, res);
    }
    cout << ans << "\n";
    return 0;
}