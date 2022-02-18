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
    vector<Int> q(n);
    for (Int i = 0; i < n; i++) cin >> q[i];

    vector<Int> par(n + n, -1);
    rep(i, n) { unite(par, q[i] - 1, i + n); }
    rep(i, m) {
        Int x, y;
        cin >> x >> y;
        x--;
        y--;
        unite(par, x, y);
    }
    Int ans = 0;
    rep(i, n) {
        if (find(par, i) == find(par, i + n)) ans++;
    }
    cout << ans << "\n";
    for (Int a : par) cout << a << " ";
    cout << endl;
    return 0;
}