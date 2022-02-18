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
    vector<Int> p(n + 1);
    for (Int i = 0; i < n; i++) cin >> p[i + 1];
    Int ans = 0;
    vector<Int> pre_process;
    rep(i, n + 1) {
        rep(j, n + 1) { pre_process.push_back(p[i] + p[j]); }
    }
    sort(pre_process.begin(), pre_process.end());

    rep(i, n + 1) {
        rep(j, n + 1) {
            auto iter = upper_bound(pre_process.begin(), pre_process.end(),
                                    m - p[i] - p[j]);
            Int tmp = p[i] + p[j] + *--iter;
            if (tmp <= m) ans = max(ans, tmp);
        }
    }
    cout << ans << "\n";

    return 0;
}