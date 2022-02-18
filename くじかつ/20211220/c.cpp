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
    Int w, h, n;
    cin >> w >> h >> n;
    Int x_min = w, y_min = h;
    Int x_max = 0, y_max = 0;
    rep(i, n) {
        Int x, y, a;
        cin >> x >> y >> a;
        if (a == 1)
            x_max = max(x_max, x);
        else if (a == 2)
            x_min = min(x_min, x);
        else if (a == 3)
            y_max = max(y_max, y);
        else if (a == 4)
            y_min = min(y_min, y);
    }
    Int ans = max(0, x_min - x_max) * max(0, y_min - y_max);
    cout << ans << "\n";
    return 0;
}