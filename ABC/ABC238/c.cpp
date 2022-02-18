#include <algorithm>
#include <atcoder/all>
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

using namespace atcoder;
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
// using lli = long long;
// using mint = modint1000000007;
using mint = modint998244353;

mint sum(Int x) { return mint(x) * (x + 1) / 2; }

int main() {
    Int n;
    cin >> n;
    mint ans = 0;
    rep(i, 100) {
        Int top = min(powl(10, i + 1) - 1, n);
        Int bottom = powl(10, i);
        ans += sum(max(0, top - bottom + 1));
    }
    cout << ans.val() << "\n";
    return 0;
}