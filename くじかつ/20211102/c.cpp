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
    Int n;
    cin >> n;
    vector<Int> a(n);
    for (Int i = 0; i < n; i++)
        cin >> a[i];
    vector<Int> res;
    rep(i, n)
    {
        res.push_back(a[i]);
        res.push_back(a[i]);
    }
    sort(res.begin(), res.end());
    reverse(res.begin(), res.end());

    Int ans = 0;
    rep_s(i, 1, n)
    {
        ans += res[i];
    }

    cout << ans << "\n";
    return 0;
}