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

Int find(vector<Int> &p, Int x) {
    if (p[x] < 0) return x;
    return p[x] = find(p, p[x]);
}

void unite(vector<Int> &p, Int x, Int y) {
    Int px = find(p, x);
    Int py = find(p, y);
    if (px == py) return;
    p[px] += p[py];
    p[py] = px;
    return;
}

int main() {
    Int n, m;
    cin >> n >> m;
    vector<Int> p(n, -1);
    vector<Int> ans;

    vector<vector<Int>> g(n);
    rep(i, m) {
        Int a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].push_back(b);
    }
    Int res = 0;
    rep_r(i, n - 1, -1) {
        ans.push_back(res);
        res++;
        rep_e(e, g[i]) {
            if (find(p, i) != find(p, e)) {
                res--;
                unite(p, i, e);
            }
        }
    }
    reverse(ans.begin(), ans.end());
    rep_e(e, ans) { cout << e << "\n"; }
    return 0;
}