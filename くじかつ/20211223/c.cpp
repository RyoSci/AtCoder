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

Int n, k;

Int f(Int a) {
    Int max_a = min(a - 1, n);
    return max(0, max_a - (a - max_a) + 1);
}

int main() {
    cin >> n >> k;
    Int ans = 0;
    rep_s(x, 2, 2 * n + 1) {
        Int y = x - k;
        if (2 <= y && y <= 2 * n) ans += f(x) * f(y);
        cout << x << " " << y << " " << f(x) << " " << f(y) << "\n";
    }
    cout << ans << "\n";
    return 0;
}