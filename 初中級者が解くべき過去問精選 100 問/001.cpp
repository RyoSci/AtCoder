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
    while (true) {
        Int n, x;
        cin >> n >> x;
        if (n == 0 && x == 0) return 0;
        Int ans = 0;
        rep_s(i, 1, n - 1) {
            rep_s(j, i + 1, n) {
                rep_s(k, j + 1, n + 1) if (i + j + k == x) ans++;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}