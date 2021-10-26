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
#define rep(i, k, n) for (int i = k; i < n; i++)

int main()
{
    Int n, k;
    cin >> n >> k;
    Int res;
    res = 0;
    for (Int i = k; i < n + 2; i++)
    {
        Int r = i * (n + n - i + 1) / 2 % MOD;
        Int l = i * (i - 1) / 2 % MOD;

        res = (res + r - l + 1) % MOD;
    }
    if (res < 0)
    {
        res += MOD;
    }
    cout << res << "\n";

    return 0;
}