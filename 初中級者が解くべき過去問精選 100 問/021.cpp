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

Int n;
vector<Int> h, s;

bool f(Int m) {
    vector<Int> tmp(n);
    rep(i, n) {
        if (m - h[i] >= 0) tmp[min(n - 1, (m - h[i]) / s[i])]++;
    }
    rep_r(i, n - 1, 0) { tmp[i - 1] += tmp[i]; }
    bool flag = true;
    rep(i, n) {
        if (tmp[i] < n - i) flag = false;
    }
    return flag;
}

int main() {
    cin >> n;
    h.resize(n);
    s.resize(n);
    for (Int i = 0; i < n; i++) cin >> h[i] >> s[i];
    Int l = -1;
    Int r = powl(10, 18);
    while (l + 1 <= r) {
        Int m = (l + r) / 2;
        if (f(m))
            r = m;
        else
            l = m + 1;
    }

    cout << r << "\n";
    return 0;
}