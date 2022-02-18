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
    vector<Int> a(n + 2);
    a[0] = 0;
    a[n + 1] = 0;
    for (Int i = 1; i < n + 1; i++) cin >> a[i];
    Int total = 0;
    rep_s(i, 1, n + 2) { total += abs(a[i] - a[i - 1]); }

    Int ans = 0;
    rep_s(i, 1, n + 1) {
        ans = total - abs(a[i] - a[i - 1]) - abs(a[i + 1] - a[i]) +
              abs(a[i + 1] - a[i - 1]);
        cout << ans << "\n";
    }
    return 0;
}