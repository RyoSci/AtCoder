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
    rep(i, m) {
        Int ai, bi;
        cin >> ai >> bi;
        ai--;
        bi--;
        g[ai].push_back(bi);
        g[bi].push_back(ai);
    }
    vector<Int> dis(n, INF);
    dis[0] = 0;
    vector<Int> ans(n, -1);
    ans[0] = 0;

    queue<Int> q;
    q.push(0);
    while (!q.empty()) {
        Int par = q.front();
        q.pop();
        rep_e(chi, g[par]) {
            if (dis[par] + 1 < dis[chi]) {
                dis[chi] = dis[par] + 1;
                ans[chi] = par;
                q.push(chi);
                cout << par << " " << chi << "\n";
            }
        }
    }
    bool flag = true;
    rep(i, n) {
        if (ans[i] == -1) flag = false;
    }

    if (flag) {
        cout << "Yes"
             << "\n";
        rep_s(i, 1, n) { cout << ans[i] + 1 << "\n"; }
    } else
        cout << "No"
             << "\n";

    return 0;
}