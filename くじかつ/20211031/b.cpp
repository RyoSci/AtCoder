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
    Int n, a, b;
    cin >> n >> a >> b;
    if ((b - a) % 2 == 0)
    {
        /* code */
        cout << (b - a) / 2 << "\n";
    }
    else
    {
        Int tmp = 0;
        if (n - b > a - 1)
        {
            /* code */
            tmp += a - 1;
            b -= tmp;
            cout << tmp + (b - 1 + 2 - 1) / 2 << "\n";
        }
        else
        {
            /* code */
            tmp += n - b;
            a += tmp;
            cout << tmp + (n - a + 2 - 1) / 2 << "\n";
        }
    }

    return 0;
}