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
#define rep_each(i, s) for (char i : s)

int main()
{
    string s;
    cin >> s;
    int abc[3];
    rep(i, 3) abc[i] = 0;
    rep_each(i, s)
    {
        if (i == 'a')
        {
            abc[0]++;
        }
        else if (i == 'b')
        {
            abc[1]++;
        }
        else
        {
            abc[2]++;
        }
    }
    sort(abc, abc + 3);

    if (abc[2] - 1 <= abc[0] && abc[2] - 1 <= abc[1])
    {
        cout << "YES"
             << "\n";
    }
    else
    {
        cout << "NO"
             << "\n";
    }

    return 0;
}