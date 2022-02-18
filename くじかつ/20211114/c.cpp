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

Int comb(Int x)
{
    return x * (x - 1) / 2;
}

int main()
{
    Int n;
    cin >> n;
    vector<Int> a(n);
    for (Int i = 0; i < n; i++)
        cin >> a[i];
    map<Int, Int> d;
    rep(i, n)
    {
        d[a[i]]++;
    }
    Int total = 0;
    for (auto x : d)
    {
        Int key = x.first;
        Int val = x.second;
        total += comb(val);
    }
    rep(i, n)
    {
        Int res;
        res = total - comb(d[a[i]]) + comb(d[a[i]] - 1);
        cout << res << "\n";
    }
    return 0;
}