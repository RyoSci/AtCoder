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

Int cnt, res;
string str;
int main()
{
    int s, t, res;
    res = 0;
    cin >> s >> t;
    rep(a, 101)
    {
        rep(b, 101)
        {
            rep(c, 101)
            {
                if (a + b + c <= s && a * b * c <= t)
                {
                    res++;
                }
            }
        }
    }
    cout << res << "\n";
    return 0;
}