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

vector<Int> tree;
vector<vector<Int>> g;

void dfs(Int par, Int root) {
    rep_e(chi, g[par]) {
        if (chi == root) continue;
        tree[chi] += tree[par];
        dfs(chi, par);
    }
}

int main() {
    Int n, q;
    cin >> n >> q;
    g.resize(n);
    rep(i, n - 1) {
        Int a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    tree.resize(n);
    rep(i, q) {
        Int p, x;
        cin >> p >> x;
        p--;
        tree[p] += x;
    }

    dfs(0, -1);

    for (Int a : tree) cout << a << " ";
    cout << endl;
    return 0;
}