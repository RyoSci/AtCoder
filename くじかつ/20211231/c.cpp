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
    string s;
    cin >> n >> s;
    vector<Int> a(n + 1);
    vector<Int> t(n + 1);
    vector<Int> c(n + 1);
    vector<Int> g(n + 1);

    rep(i, n) {
        if (s[i] == 'A') a[i + 1]++;
        if (s[i] == 'T') t[i + 1]++;
        if (s[i] == 'C') c[i + 1]++;
        if (s[i] == 'G') g[i + 1]++;
    }

    rep(i, n) {
        a[i + 1] += a[i];
        t[i + 1] += t[i];
        c[i + 1] += c[i];
        g[i + 1] += g[i];
    }
    Int ans = 0;
    rep(i, n) {
        rep_s(j, i + 1, n + 1) {
            if (a[j] - a[i] == t[j] - t[i] && c[j] - c[i] == g[j] - g[i]) ans++;
        }
    }
    cout << ans << "\n";
    return 0;
}