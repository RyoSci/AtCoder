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

vector<Int> d(100), f(100);
vector<vector<Int>> g(100);
Int cnt = 0;
vector<bool> seen(100);

void dfs(Int par) {
    if (seen[par]) return;
    seen[par] = true;
    cnt++;
    d[par] = cnt;
    rep_e(chi, g[par]) { dfs(chi); }
    cnt++;
    f[par] = cnt;
}

int main() {
    Int n;
    cin >> n;
    d.resize(n);
    f.resize(n);
    g.resize(n);
    seen.resize(n, false);
    rep(i, n) {
        Int u, k;
        cin >> u >> k;
        rep(j, k) {
            Int v;
            cin >> v;
            v--;
            g[u - 1].push_back(v);
        }
        sort(g[u - 1].begin(), g[u - 1].end());
    }
    rep(i, n) {
        if (seen[i]) continue;
        dfs(i);
    }

    rep(i, n) { cout << i + 1 << " " << d[i] << " " << f[i] << "\n"; }
    return 0;
}