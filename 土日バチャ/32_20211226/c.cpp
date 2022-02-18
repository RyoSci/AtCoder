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
    vector<pair<Int, string>> p;
    rep_e(x, d) { p.push_back({-x.second, x.first}); }
    sort(p.begin(), p.end());
    Int max_num = p[0].first;
    rep_e(x, p) {
        if (max_num != x.first) return 0;
        cout << x.second << "\n";
    }

    return 0;
}