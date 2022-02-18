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
    // Int n = 3000;
    // vector<Int> x(n), y(n);
    // rep(i, n) { x[i] = i + 1, y[i] = i + 1; }
    // map<P, Int> dict;
    // rep(i, n) { dict[make_pair(x[i], y[i])] = 1; }
    Int n;
    cin >> n;
    vector<Int> x(n), y(n);
    rep(i, n) { cin >> x[i] >> y[i]; }
    // set<P> dict;
    // rep(i, n) { dict.insert(make_pair(x[i], y[i])); }
    map<P, Int> dict;
    rep(i, n) { dict[make_pair(x[i], y[i])] = 1; }

    Int ans = 0;
    rep(i, n - 1) {
        rep_s(j, i + 1, n) {
            Int dx = x[j] - x[i];
            Int dy = y[j] - y[i];
            // if (dict.count(make_pair(x[i] + dy, y[i] - dx)) > 0 &&
            //     dict.count(make_pair(x[j] + dy, y[j] - dx)) > 0)
            //     if (ans < dx * dx + dy * dy) ans = dx * dx + dy * dy;
            if (dict.count(make_pair(x[i] + dy, y[i] - dx)) > 0 &&
                dict.count(make_pair(x[j] + dy, y[j] - dx)) > 0)
                if (ans < dx * dx + dy * dy) ans = dx * dx + dy * dy;
        }
    }
    cout << ans << "\n";
    return 0;
}