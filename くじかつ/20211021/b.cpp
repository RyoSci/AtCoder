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
#define rep_one(i, n) for (int i = 1; i < n; i++)

int main()
{
    int n;
    cin >> n;
    vector<int> a(n+1);

    rep_one(x, 101)
    {
        rep_one(y, 101)
        {
            rep_one(z, 101)
            {
                int tmp;
                tmp = x * x + y * y + z * z + x * y + y * z + z * x;
                if (0 < tmp && tmp <= n)
                {
                    /* code */
                    a[tmp]++;
                    // cout << tmp << a[tmp] << "\n";
                }
            }
        }
    }

    rep_one(i, n + 1)
    {
        cout << a[i] << "\n";
    }
    return 0;
}