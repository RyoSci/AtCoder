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

Int x, y, ans;
int main()
{
    vector<Int> v = {300000, 200000, 100000};
    cin >> x >> y;
    if (x == 1 and y == 1)
    {
        ans = 400000 + 300000 * 2;
    }
    else
    {
        if (x <= 3)
        {
            ans += v[x - 1];
        }
        if (y <= 3)
        {
            ans += v[y - 1];
        }
    }
    cout << ans << endl;
    return 0;
}