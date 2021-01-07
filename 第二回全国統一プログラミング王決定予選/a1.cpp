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

Int n, ans;
int main()
{
    cin >> n;
    for (int i = 1; i < n; i++)
    {
        if (i >= n - i)
        {
            break;
        }
        ans += 1;
    }
    cout << ans << endl;
    return 0;
}