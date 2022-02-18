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
    Int n;
    cin >> n;
    vector<Int> w(n);
    for (Int i = 0; i < n; i++) cin >> w[i];
    Int total = 0;
    rep(i, n) { total += w[i]; }
    Int ans = powl(10, 18);
    Int now = 0;
    rep(i, n - 1) {
        now += w[i];
        total -= w[i];
        ans = min(ans, abs(total - now));
    }
    cout << ans << "\n";
    return 0;
}