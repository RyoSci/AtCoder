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
    Int r, c;
    cin >> r >> c;
    vector<vector<Int>> a(r, vector<Int>(c));
    rep(i, r) {
        rep(j, c) { cin >> a[i][j]; }
    }
    Int ans = 0;
    rep(i, 1 << r) {
        vector<int> bit(r);
        rep(j, r) {
            if (i >> j & 1) bit[j] = 1;
        }
        Int cnt = 0;
        rep(j, c) {
            Int tmp = 0;
            rep(k, r) {
                if (bit[k])
                    tmp += a[k][j] ^ 1;
                else
                    tmp += a[k][j];
            }
            cnt += max(tmp, r - tmp);
        }
        ans = max(ans, cnt);
    }
    cout << ans << "\n";
    return 0;
}