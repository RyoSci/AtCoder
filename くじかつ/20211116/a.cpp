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
#include <iomanip>
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
    int n;
    cin >> n;
    if (n == 25)
    {
        /* code */
        cout << "Christmas"
             << "\n";
    }
    else if (n == 24)
    {
        /* code */
        cout << "Christmas Eve"
             << "\n";
    }
    else if (n == 23)
    {
        cout << "Christmas Eve Eve"
             << "\n";
        /* code */
    }
    else
    {
        /* code */
        cout << "Christmas Eve Eve Eve"
             << "\n";
    }

    return 0;
}