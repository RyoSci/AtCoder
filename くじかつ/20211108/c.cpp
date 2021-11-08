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
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> x(b);
    int mod = 1;
    int i = 1;
    while (true)
    {
        mod = a * i;
        mod %= b;
        /* code */
        if (x[mod] == 1)
        {
            /* code */
            break;
        }
        x[mod] = 1;
        i++;
    }
    bool ans = false;
    rep(i, b)
    {
        if (x[i] == 1 && i == c)
        {
            /* code */
            ans = true;
        }
    }

    cout << (ans ? "YES" : "NO") << "\n";
    return 0;
}