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

int main() {
    Int n;
    cin >> n;
    vector<Int> t(n), k(n);
    vector<vector<Int>> a(n);
    rep(i, n) {
        Int ti, ki;
        cin >> ti >> ki;
        t[i] = ti;
        rep(j, ki) {
            Int ai;
            cin >> ai;
            a[i].push_back(ai);
        }
    }
    vector<bool> used(n, false);
    used[n - 1] = true;
    rep_r(i, n - 1, -1) {
        if (!used[i]) continue;
        for (auto x : a[i]) {
            used[x - 1] = true;
        }
    }
    Int ans = 0;
    rep(i, n) {
        if (used[i]) ans += t[i];
    }
    cout << ans << "\n";
    return 0;
}