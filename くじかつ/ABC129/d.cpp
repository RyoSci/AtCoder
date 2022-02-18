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
    Int h, w;
    cin >> h >> w;
    vector<string> s(h);
    rep(i, h) { cin >> s[i]; }
    vector<vector<Int>> yoko(h, vector<Int>(w));
    vector<vector<Int>> tate(h, vector<Int>(w));

    rep(i, h) {
        Int j = 0;
        Int cnt = 0;
        Int start = w;
        while (j < w) {
            if (s[i][j] == '.') {
                start = min(start, j);
                j++;
                cnt++;
            } else {
                rep_s(k, start, j) { yoko[i][k] = cnt; }
                cnt = 0;
                j++;
                start = w;
            }
        }
        if (cnt > 0) {
            rep_s(k, start, w) { yoko[i][k] = cnt; }
        }
    }

    rep(j, w) {
        Int i = 0;
        Int cnt = 0;
        Int start = h;
        while (i < h) {
            if (s[i][j] == '.') {
                start = min(start, i);
                i++;
                cnt++;
            } else {
                rep_s(k, start, i) { tate[k][j] = cnt; }
                cnt = 0;
                i++;
                start = h;
            }
        }
        if (cnt > 0) {
            rep_s(k, start, h) { tate[k][j] = cnt; }
        }
    }
    Int ans = 0;
    rep(i, h) {
        rep(j, w) { ans = max(ans, tate[i][j] + yoko[i][j] - 1); }
    }
    cout << ans << "\n";
    return 0;
}