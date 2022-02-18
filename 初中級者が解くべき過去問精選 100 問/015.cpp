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
    vector<double> x(n), y(n);
    for (Int i = 0; i < n; i++) cin >> x[i] >> y[i];
    vector<Int> b(n);
    rep(i, n) { b[i] = i; }
    double ans = 0.0;
    double cnt = 0.0;
    do {
        double res = 0.0;
        rep(i, n - 1) {
            double dx = x[b[i]] - x[b[i + 1]];
            double dy = y[b[i]] - y[b[i + 1]];
            res += pow(dx * dx + dy * dy, 0.5);
        }
        ans += res;
        cnt += 1.0;
    } while (next_permutation(b.begin(), b.end()));
    cout << std::fixed << std::setprecision(15) << ans / cnt << endl;
    return 0;
}