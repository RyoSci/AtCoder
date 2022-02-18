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

void dfs(Int pair, Int root, Int k, Int rest, vector<vector<Int>> &g, Int &res)
{
    for (Int chi : g[pair])
    {
        if (chi == root)
        {
            /* code */
            continue;
        }
        rest--;
        res *= rest;
        res %= MOD;
        dfs(chi, pair, k, max(k - 1, rest), g, res);
    }
}

int main()
{
    Int n, k;
    cin >> n >> k;
    vector<vector<Int>> g(n);
    rep(i, n - 1)
    {
        Int a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    Int res = k;
    dfs(0, -1, k, k, g, res);
    cout << res << "\n";
    return 0;
}