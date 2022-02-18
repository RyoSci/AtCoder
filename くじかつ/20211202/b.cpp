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
    Int n, k, q;
    cin >> n >> k >> q;
    vector<Int> a(n, k - q);
    rep(i, q) {
        Int ai;
        cin >> ai;
        a[ai - 1]++;
    }
    Int ans = 0;
    rep_e(x, a) {
        if (x > 0)
            cout << "Yes"
                 << "\n";
        else
            cout << "No"
                 << "\n";
    }

    return 0;
}