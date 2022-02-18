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
    int n;
    cin >> n;
    vector<int> x(n);
    for (int i = 0; i < n; i++)
        cin >> x[i];

    vector<int> y(n);
    rep(i, n)
    {
        y[i] = x[i];
    }
    sort(x.begin(), x.end());
    rep(i, n)
    {
        if (y[i] <= x[n / 2 - 1])
        {
            cout << x[n / 2] << "\n";
        }
        else
        {
            cout << x[n / 2 - 1] << "\n";
        }
    }
    return 0;
}