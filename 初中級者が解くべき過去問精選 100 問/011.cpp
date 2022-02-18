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
    vector<vector<Int>> s(m);
    rep(i, m) {
        Int k;
        cin >> k;
        rep(j, k) {
            Int si;
            cin >> si;
            s[i].push_back(si);
        }
    }
    vector<Int> p(m);
    for (Int i = 0; i < m; i++) cin >> p[i];

    Int ans = 0;
    rep(i, 1 << n) {
        vector<bool> st(n);
        rep(j, n) {
            if (i >> j & 1) st[j] = true;
        }
        vector<Int> p_dash(m);
        rep(j, m) {
            Int tmp = 0;
            rep(k, s[j].size()) {
                if (st[s[j][k] - 1]) tmp ^= 1;
            }
            p_dash[j] = tmp;
        }
        if (p == p_dash) ans++;
    }

    cout << ans << "\n";
    return 0;
}