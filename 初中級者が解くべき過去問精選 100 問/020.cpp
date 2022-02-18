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
    vector<Int> a(n);
    for (Int i = 0; i < n; i++) cin >> a[i];
    vector<Int> b(n);
    for (Int i = 0; i < n; i++) cin >> b[i];
    vector<Int> c(n);
    for (Int i = 0; i < n; i++) cin >> c[i];

    sort(a.begin(), a.end());
    sort(c.begin(), c.end());

    Int ans = 0;
    rep(i, n) {
        auto iter1 = lower_bound(a.begin(), a.end(), b[i]);
        auto iter2 = upper_bound(c.begin(), c.end(), b[i]);
        ans += distance(a.begin(), iter1) * distance(iter2, c.end());
    }
    cout << ans << "\n";
    return 0;
}