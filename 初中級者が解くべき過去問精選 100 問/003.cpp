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
    set<char> t = {'A', 'C', 'G', 'T'};
    Int ans = 0;
    Int now = 0;
    Int n = s.size();
    rep(i, n) {
        if (t.count(s[i]) > 0)
            now++;
        else {
            now = 0;
        }
        ans = max(ans, now);
    }
    cout << ans << "\n";
    return 0;
}