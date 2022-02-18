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

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    vector<int> b(n);
    for (int i = 0; i < n; i++)
        cin >> b[i];

    int res;
    res = 0;
    rep(x, 1001)
    {
        bool flag;
        flag = true;
        rep(i, n)
        {
            if (a[i] <= x && x <= b[i])
            {
                /* code */
                continue;
            }
            else
            {
                flag = false;
                break;
            }
        }
        if (flag)
        {
            /* code */
            res++;
        }
    }
    cout << res << "\n";
    return 0;
}