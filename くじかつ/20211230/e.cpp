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
    vector<Int> a(n + 1);
    for (Int i = 1; i < n + 1; i++) cin >> a[i];
    rep(i, n) { a[i + 1] += a[i]; }
    map<Int, Int> mod;
    rep(i, n + 1) { mod[a[i] % m]++; }

    Int ans = 0;
    rep_e(x, mod) {
        Int key = x.first;
        Int val = x.second;
        ans += val * (val - 1) / 2;
    }
    cout << ans << "\n";
    return 0;
}