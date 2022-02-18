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

Int a[51];

Int f(Int x, Int n, vector<vector<Int>> a)
{
    if (n == 1)
    {
        if (x == 1)
            return 0;
        else if (x == 2)
            return 1;
        else if (x == 3)
            return 2;
        else
            return 3;
    }

    if (x == a[n][0])
        return 0;
    else if (a[n][0] < x && x < a[n][1])
        return f(x - a[n][0], n - 1, a);
    else if (x == a[n][1])
        return a[n - 1][1] + 1;
    else if (a[n][1] < x && x < a[n][2])
        return f(x - a[n][1], n - 1, a) + a[n - 1][1];
    else
        return a[n - 1][1] * 2 + 1;
}

int main()
{
    Int n, x;
    cin >> n >> x;
    vector<vector<Int>> a(3, vector<Int>(n + 1));
    a[1] = {1, 3, 5};
    for (int i = 1; i < n; i++)
    {
        a[i + 1][0] = a[i][0];
        a[i + 1][1] = a[i][1] * 2 + 1;
        a[i + 1][2] = a[i][2] * 2 + 3;
    }

    cout << f(x, n, a) << "\n";

    return 0;
}