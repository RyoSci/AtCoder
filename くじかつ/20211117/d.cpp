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

vector<int> seen(100000 + 10, 0);
void dfs(int pair, int root, vector<int> &ans, vector<int> &c, vector<vector<int>> &g)
{
    seen[c[pair]]++;
    for (auto chi : g[pair])
    {
        if (chi == root)
        {
            /* code */
            continue;
        }
        if (!seen[c[chi]])
        {
            /* code */
            ans.push_back(chi);
        }

        dfs(chi, pair, ans, c, g);
    }
    seen[c[pair]]--;
}

int main()
{
    int n;
    cin >> n;
    vector<int> c(n);
    for (int i = 0; i < n; i++)
        cin >> c[i];
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
    vector<int> ans;
    ans.push_back(0);
    dfs(0, -1, ans, c, g);
    sort(ans.begin(), ans.end());
    for (auto i : ans)
    {
        cout << i + 1 << "\n";
    }

    return 0;
}