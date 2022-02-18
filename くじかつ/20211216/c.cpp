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
    Int x, y, a, b;
    cin >> x >> y >> a >> b;
    Int ans = 0;
    if (x * (a - 1) >= b) {
        ans = (y - x) / b;
        if ((y - x) % b == 0) ans--;
        cout << ans << "\n";
    } else {
        Int now = x;
        rep_s(i, 1, 100) {
            if (now >= y) {
                break;
            } else if (now * a <= now + b && now * a < y) {
                ans++;
                now *= a;
            } else {
                ans += (y - now) / b;
                if ((y - now) % b == 0) ans--;
                break;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}