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
    Int d;
    cin >> d;
    Int n;
    cin >> n;
    Int m;
    cin >> m;
    vector<Int> D(n + 1);
    D[0] = 0;
    D[n] = d;
    for (Int i = 1; i < n; i++) cin >> D[i];
    sort(D.begin(), D.end());

    vector<Int> k(m);
    for (Int i = 0; i < m; i++) cin >> k[i];

    Int ans = 0;
    rep(i, m) {
        auto iter = lower_bound(D.begin(), D.end(), k[i]);
        Int dis1 = *iter - k[i];
        iter--;
        Int dis2 = k[i] - *iter;
        if (dis1 < 0 | dis2 < 0) cout << dis1 << " " << dis2 << "\n";
        ans += min(dis1, dis2);
    }
    cout << ans << "\n";
    return 0;
}