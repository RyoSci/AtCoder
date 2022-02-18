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
    string s;
    cin >> s;
    Int ans = 0;
    rep(i, 1000) {
        string t = to_string(i);
        string nt = t;
        rep(j, 3 - t.length()) { nt = "0" + nt; }
        Int cnt = 0;
        rep(j, n) {
            if (cnt == 3) break;
            if (nt[cnt] == s[j]) {
                cnt++;
            }
        }
        if (cnt == 3) {
            ans++;
        }
    }
    cout << ans << "\n";
    return 0;
}