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

Int n, t, a, res;
int main()
{
    cin >> n >> t;
    for (int i = 0; i < n - 1; i++)
    {
        cin >> a;
        res += a;
    }
    res = (res + t - 1) / t;
    cout << res << endl;
    return 0;
}