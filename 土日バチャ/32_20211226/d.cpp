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
    string s;
    cin >> s;
    Int m = s.length();
    vector<Int> n(m + 1);
    rep(i, m) { n[i + 1] = s[i] - '0'; }
    vector<Int> ans(m + 1), rest(m + 1);
    rep_r(i, m, -1) {
        if (n[i] + ans[i] >= 6) {
            ans[i - 1]++;
            ans[i] = 0;
        } else {
            ans[i] += n[i];
        }
    }
    rep_r(i, m, -1) {
        if (ans[i] - n[i] < 0) {
            rest[i - 1]--;
            rest[i] += ans[i] + 10 - n[i];
        } else
            rest[i] += ans[i] - n[i];
    }
    Int res = 0;
    rep(i, m + 1) { res += ans[i] + rest[i]; }
    cout << res << "\n";
    for (Int a : ans) cout << a << " ";
    cout << endl;
    for (Int a : n) cout << a << " ";
    cout << endl;
    for (Int a : rest) cout << a << " ";
    cout << endl;
    return 0;
}