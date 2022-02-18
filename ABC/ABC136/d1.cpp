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
    string s;
    cin >> s;
    Int n = s.length();
    Int m = 20;
    vector<vector<Int>> next(m + 1, vector<Int>(n));
    rep(i, n) {
        if (s[i] == 'R')
            next[0][i] = i + 1;
        else
            next[0][i] = i - 1;
    }

    rep(i, m) {
        rep(j, n) { next[i + 1][j] = next[i][next[i][j]]; }
    }
    vector<Int> ans(n);

    rep(i, n) { ans[next[20][i]]++; }

    for (Int a : ans) cout << a << " ";
    cout << endl;
    return 0;
}