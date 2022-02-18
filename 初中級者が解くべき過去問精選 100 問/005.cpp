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
    Int a, b, c, x, y;
    cin >> a >> b >> c >> x >> y;
    Int ans = powl(10, 18);
    for (Int i = 0; i < max(x, y) * 2 + 10; i += 2) {
        Int tmp = max(0, x - i / 2) * a + max(0, y - i / 2) * b + c * i;
        ans = min(ans, tmp);
    }
    cout << ans << "\n";
    return 0;
}