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
    Int n = 1 << 20;
    set<Int> a;
    rep(i, n) { a.insert(i); }
    a.insert(INF);
    Int q;
    cin >> q;
    Int h;
    map<Int, Int> ans;
    rep(i, q) {
        Int t, x;
        cin >> t >> x;
        if (t == 1) {
            h = x % n;
            auto iter = a.lower_bound(h);
            Int num = *iter;
            if (num == INF) {
                auto iter = a.lower_bound(0);
                Int num = *iter;
            }
            ans[num] = x;
            a.erase(num);
        } else {
            if (ans.count(x % n))
                cout << ans[x % n] << "\n";
            else
                cout << -1 << "\n";
        }
    }
    rep_e(aa, ans) { cout << aa.first << " " << aa.second << "\n"; }
    return 0;
}