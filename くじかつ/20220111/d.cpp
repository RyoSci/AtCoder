#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
#define MOD 1000000007
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (Int i = 0; i < n; i++)
#define rep_r(i, k, n) for (Int i = k; i > n; i--)
#define rep_s(i, k, n) for (Int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)

int main() {
    Int n, m;
    cin >> n >> m;
    vector<vector<Int>> g(n);
    vector<Int> par(n);
    rep(i, m) {
        Int a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].push_back(b);
        par[b]++;
    }
    priority_queue<Int> q;
    rep(i, n) {
        if (par[i] == 0) q.push(-i);
    }
    vector<Int> ans;
    while (q.size() > 0) {
        Int x = -q.top();
        q.pop();
        ans.push_back(x);
        sort(g[x].begin(), g[x].end());
        rep_e(chi, g[x]) {
            par[chi]--;
            if (par[chi] == 0) q.push(-chi);
        }
    }
    if (ans.size() == n) {
        for (Int a : ans) cout << a + 1 << " ";
        cout << endl;
    } else
        cout << -1 << "\n";
    return 0;
}