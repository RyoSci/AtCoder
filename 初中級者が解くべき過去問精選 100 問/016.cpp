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
    vector<Int> p(n);
    for (Int i = 0; i < n; i++) cin >> p[i];
    vector<Int> q(n);
    for (Int i = 0; i < n; i++) cin >> q[i];
    vector<Int> r(n);
    rep(i, n) { r[i] = i + 1; }
    Int a, b;
    Int cnt = 0;
    do {
        if (r == p) a = cnt;
        if (r == q) b = cnt;
        cnt++;
    } while (next_permutation(r.begin(), r.end()));

    cout << abs(a - b) << "\n";
    return 0;
}