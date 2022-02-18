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

Int f(Int l, Int r, Int x) {
    if (l < x)
        return min(r - l + 1, x - l);
    else
        return 0;
}

int main() {
    Int n;
    cin >> n;
    vector<Int> l(n), r(n);
    rep(i, n) { cin >> l[i] >> r[i]; }
    double ans = 0.0;
    rep(i, n) {
        rep_s(j, l[i], r[i] + 1) {
            rep_s(k, i + 1, n) {
                ans += (double)f(l[k], r[k], j) / (r[k] - l[k] + 1) /
                       (r[i] - l[i] + 1);
            }
        }
    }
    // cout << ans << "\n";
    //小数点以下の長さを指定
    cout << fixed << setprecision(15) << ans << endl;
    return 0;
}