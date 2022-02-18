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

Int f(Int x, Int k)
{
    string pre = to_string(x);
    Int n = pre.length();
    Int res = 0;

    for (Int i = n - 1; i > -1; i--)
    {
        res += ((Int)pre[i] - '0') * pow(k, n - 1 - i);
    }
    return res;
}

int main()
{
    Int k;
    cin >> k;
    Int a, b;
    cin >> a >> b;

    cout << f(a, k) * f(b, k) << "\n";

    return 0;
}