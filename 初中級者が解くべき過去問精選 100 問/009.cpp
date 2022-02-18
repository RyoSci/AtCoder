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
    Int m;
    cin >> m;
    vector<Int> mx(m), my(m);
    rep(i, m) { cin >> mx[i] >> my[i]; }
    Int n;
    cin >> n;
    set<P> dict;
    vector<Int> nx(n), ny(n);
    rep(i, n) {
        Int xi, yi;
        cin >> xi >> yi;
        dict.insert(make_pair(xi, yi));
        nx[i] = xi;
        ny[i] = yi;
    }

    rep(i, n) {
        Int dx = nx[i] - mx[0];
        Int dy = ny[i] - my[0];
        bool flag = true;
        rep(j, m) {
            if (dict.count(make_pair(mx[j] + dx, my[j] + dy)) == 0) {
                flag = false;
                break;
            }
        }
        if (flag) cout << dx << " " << dy << "\n";
    }

    return 0;
}