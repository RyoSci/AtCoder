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

Int h, w;
vector<string> s;

Int f1(Int x, Int y) {
    Int ans = 0;
    rep_s(i, x, h) {
        if (s[i][y] == '#')
            break;
        else
            ans++;
    }
    return ans;
}
Int f2(Int x, Int y) {
    Int ans = 0;
    for (Int i = x; i >= 0; i--) {
        if (s[i][y] == '#')
            break;
        else
            ans++;
    }
    return ans;
}
Int f3(Int x, Int y) {
    Int ans = 0;
    rep_s(i, y, w) {
        if (s[x][i] == '#')
            break;
        else
            ans++;
    }
    return ans;
}
Int f4(Int x, Int y) {
    Int ans = 0;
    for (Int i = y; i >= 0; i--) {
        if (s[x][i] == '#')
            break;
        else
            ans++;
    }
    return ans;
}

int main() {
    cin >> h >> w;
    s.resize(h);
    rep(i, h) { cin >> s[i]; }

    Int ans = 0;
    rep(i, h) {
        rep(j, w) {
            Int res = -3;
            res += f1(i, j);
            res += f2(i, j);
            res += f3(i, j);
            res += f4(i, j);
            ans = max(ans, res);
        }
    }
    cout << ans << "\n";
    return 0;
}