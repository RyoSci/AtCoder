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
    Int n;
    cin >> n;
    vector<Int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    vector<Int> b(n);
    for (int i = 0; i < n; i++)
        cin >> b[i];

    Int max_cnt = 0;
    Int res = 0;
    rep(i, n)
    {
        max_cnt = max(max_cnt, a[i]);
        res = max(res, max_cnt * b[i]);
        cout << res << "\n";
    }

    return 0;
}