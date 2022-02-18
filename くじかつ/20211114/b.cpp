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
    string n;
    cin >> n;
    int m = n.length();
    int res = INF;
    for (Int i = 0; i < (1 << m); i++)
    {
        int tmp = 0;
        int cnt = 0;
        for (Int j = 0; j < m; j++)
        {
            if ((i >> j) & 1)
            {
                /* code */
                tmp += n[j] - '0';
            }
            else
            {
                cnt++;
            }
        }
        if (tmp % 3 == 0 && tmp != 0)
        {
            /* code */
            res = min(res, cnt);
        }
    }
    if (res == INF)
    {
        /* code */
        cout << -1 << "\n";
    }
    else
    {
        cout << res << "\n";
    }

    return 0;
}