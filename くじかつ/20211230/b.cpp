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
    Int n, k;
    cin >> n >> k;
    vector<Int> res(n);
    rep(i, k) {
        Int d;
        cin >> d;
        Int a;
        for (Int i = 0; i < d; i++) {
            cin >> a;
            res[a - 1]++;
        }
    }
    Int ans = 0;
    rep(i, n) {
        if (res[i] == 0) ans++;
    }
    cout << ans << "\n";
    return 0;
}