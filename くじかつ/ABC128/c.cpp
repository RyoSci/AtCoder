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
    vector<Int> k(m);
    vector<vector<Int>> s(m);

    rep(i, m) {
        cin >> k[i];
        rep(j, k[i]) {
            Int si;
            cin >> si;
            s[i].push_back(si);
        }
    }
    vector<Int> p(m);
    for (Int i = 0; i < m; i++) cin >> p[i];

    Int ans = 0;
    rep(i, (1 << n)) {
        vector<Int> tmp(n);
        rep(j, n) {
            if ((i >> j) & 1) {
                tmp[j] = 1;
            }
        }

        vector<Int> bulb(m);
        rep(j, m) {
            rep(kj, k[j]) {
                if (tmp[s[j][kj] - 1] == 1) bulb[j] ^= 1;
            }
        }
        bool flag = true;
        rep(j, m) {
            if (bulb[j] != p[j]) flag = false;
        }
        if (flag) ans++;
    }

    cout << ans << "\n";
    return 0;
}