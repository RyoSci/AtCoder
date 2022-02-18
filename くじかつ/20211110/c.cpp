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
    int n, m;
    cin >> n >> m;
    vector<P> ab(n);
    vector<P> cd(m);
    rep(i, n)
    {
        Int a, b;
        cin >> a >> b;
        ab[i] = P(a, b);
    }
    rep(i, m)
    {
        Int c, d;
        cin >> c >> d;
        cd[i] = P(c, d);
    }
    rep(i, n)
    {
        Int res = INF;
        Int index = 0;
        Int a = ab[i].first;
        Int b = ab[i].second;
        rep(j, m)
        {
            Int c = cd[j].first;
            Int d = cd[j].second;
            Int tmp = abs(a - c) + abs(b - d);
            if (tmp < res)
            {
                /* code */
                res = tmp;
                index = j;
            }
        }
        cout << index + 1 << "\n";
    }

    return 0;
}