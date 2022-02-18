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
// #include <atcoder/all>
// #include <atcoder/modint>
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;

int main() {
    Int n;
    cin >> n;
    vector<vector<Int>> g(n);
    rep(i, n) {
        Int u, k;
        cin >> u >> k;
        rep(j, k) {
            Int v;
            cin >> v;
            g[u - 1].push_back(v - 1);
        }
    }
    vector<Int> dis(n, INF);
    dis[0] = 0;
    queue<Int> q;
    q.push(0);
    while (!q.empty()) {
        Int par = q.front();
        q.pop();
        rep_e(chi, g[par]) {
            if (dis[par] + 1 < dis[chi]) {
                dis[chi] = dis[par] + 1;
                q.push(chi);
            }
        }
    }
    rep(i, n) {
        cout << i + 1 << " ";
        if (dis[i] == INF)
            cout << -1 << "\n";
        else
            cout << dis[i] << "\n";
    }

    return 0;
}