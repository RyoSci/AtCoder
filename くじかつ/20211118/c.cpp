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

void dfs(int pair, int root, vector<vector<int>> &g, vector<int> &res)
{
    res.push_back(pair);
    for (auto chi : g[pair])
    {
        if (chi == root)
        {
            /* code */
            continue;
        }
        dfs(chi, pair, g, res);
        res.push_back(pair);
    }

    return;
}

int main()
{
    int n;
    cin >> n;
    vector<vector<int>> g(n);
    rep(i, n - 1)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    rep(i, n)
    {
        sort(g[i].begin(), g[i].end());
    }
    vector<int> res;

    dfs(0, -1, g, res);

    for (int i : res)
    {
        cout << i + 1 << "\n";
    }

    return 0;
}