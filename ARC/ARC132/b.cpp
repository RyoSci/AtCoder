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
    vector<Int> p(n);
    for (Int i = 0; i < n; i++) cin >> p[i];
    bool per;
    if (p[0] + 1 == p[1] | (p[0] + 1) % n == p[1])
        per = true;
    else
        per = false;

    Int ans;
    if (per) {
        int l = 1, r = 0;
        rep_s(i, 0, n - 1) {
            if (p[i] + 1 == p[i + 1])
                l++;
            else {
                r = n - l;
                break;
            }
        }
        if (l <= r + 2) {
            ans = l;
        } else {
            if (r > 0) {
                ans = 1 + r + 1;
                // cout << l << " " << r << "\n";
            } else {
                ans = r;
                // cout << l << " " << r << "\n";
            }
        }
    } else {
        int l = 1, r = 0;
        rep_s(i, 0, n - 1) {
            if (p[i] - 1 == p[i + 1]) {
                l++;
            } else {
                r = n - l;
                break;
            }
        }
        if (l <= r) {
            ans = l + 1;
            // cout << l << " " << r << "\n";
        } else {
            ans = r + 1;
            // cout << l << " " << r << "\n";
        }
    }
    cout << ans << "\n";
    return 0;
}