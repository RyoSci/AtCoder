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
    vector<Int> s(n);
    for (Int i = 0; i < n; i++) cin >> s[i];
    set<Int> t;
    rep_s(a, 1, 250 + 10) {
        rep_s(b, 1, 250 + 10) { t.insert(4 * a * b + 3 * a + 3 * b); }
    }
    Int ans = 0;
    rep_e(x, s) {
        if (!t.count(x)) ans++;
    }
    cout << ans << "\n";
    return 0;
}