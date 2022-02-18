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
    Int n, k;
    cin >> n >> k;
    vector<Int> a(n);
    for (Int i = 0; i < n; i++) cin >> a[i];
    Int ans = powl(10, 18);
    rep_s(i, 0, 1 << n) {
        vector<Int> bit(n);
        Int cnt = 0;
        rep(j, n) {
            if (i >> j & 1) {
                bit[j] = 1;
                cnt++;
            }
        }

        Int tmp = 0;
        Int pre = a[0];
        rep_s(j, 1, n) {
            if (bit[j]) {
                tmp += max(0, pre + 1 - a[j]);
                pre = max(pre + 1, a[j]);
            }
            pre = max(pre, a[j]);
        }

        if (cnt >= k) ans = min(ans, tmp);
    }
    cout << ans << "\n";
    return 0;
}