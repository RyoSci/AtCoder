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
    vector<string> s(n);
    vector<Int> p(n);
    rep(i, n) { cin >> s[i] >> p[i]; }
    vector<tuple<string, Int, Int>> res;
    rep(i, n) { res.push_back(make_tuple(s[i], -p[i], i)); }
    sort(res.begin(), res.end());
    rep(i, n) { cout << get<2>(res[i]) + 1 << "\n"; }

    return 0;
}