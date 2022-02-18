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
    map<string, Int> d;
    rep(i, n) {
        string s;
        cin >> s;
        d[s]++;
    }
    Int m;
    cin >> m;
    rep(i, m) {
        string t;
        cin >> t;
        d[t]--;
    }
    Int ans = 0;
    rep_e(x, d) { ans = max(ans, x.second); }
    cout << ans << "\n";
    return 0;
}