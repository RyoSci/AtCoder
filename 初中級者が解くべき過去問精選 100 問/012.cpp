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
    Int n, m;
    cin >> n >> m;
    vector<Int> x(m), y(m);
    rep(i, m) { cin >> x[i] >> y[i]; }

    vector<vector<Int>> rel(n, vector<Int>(n));
    rep(i, m) {
        x[i]--;
        y[i]--;
        rel[x[i]][y[i]] = 1;
    }

    Int ans = 1;
    rep(i, 1 << n) {
        vector<Int> cand(n);
        Int cnt = 0;
        rep(j, n) {
            if (i >> j & 1) {
                cand[j] = 1;
                cnt++;
            }
        }

        bool flag = true;
        rep(j, n - 1) {
            rep_s(k, j + 1, n) {
                if (cand[j] && cand[k]) {
                    if (rel[j][k])
                        continue;
                    else
                        flag = false;
                }
            }
        }
        if (flag) {
            ans = max(ans, cnt);
        }
    }
    cout << ans << "\n";
    return 0;
}