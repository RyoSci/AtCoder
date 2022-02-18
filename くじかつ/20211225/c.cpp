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
    vector<string> a(h);
    rep(i, h) {
        string s;
        cin >> a[i];
    }
    vector<Int> ni = {1, 0};
    vector<Int> nj = {0, 1};
    Int cnt = 0;
    rep(i, h) { rep(j, w) if (a[i][j] == '#') cnt++; }
    rep(i, h) {
        rep(j, w) if (a[i][j] == '#') {
            if (i == h - 1 && j == w - 1) break;
            bool flag = false;
            rep(k, 2) {
                Int ii = i + ni[k];
                Int jj = j + nj[k];
                if (ii < h && jj < w && a[ii][jj] == '#') flag ^= true;
            }
            if (!flag) {
                cout << "Impossible"
                     << "\n";
                return 0;
            }
        }
    }
    if (cnt == h + w - 1)
        cout << "Possible"
             << "\n";
    else
        cout << "Impossible"
             << "\n";
    return 0;
}