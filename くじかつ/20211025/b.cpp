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
#define cal(x) x *(x + 1) / 2

int main()
{

    Int a, b, c;
    cin >> a >> b >> c;
    Int mod;
    mod = 998244353;
    Int res;
    res = 1;
    res *= cal(a) % mod;
    res *= cal(b) % mod;
    res *= cal(c) % mod;
    cout << res % mod << "\n";
    return 0;
}