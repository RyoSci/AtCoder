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
#define rep(i, n) for (int i = 0; i < n; i++)
#define rep_r(i, k, n) for (int i = k; i > n; i--)
#define rep_s(i, k, n) for (int i = k; i < n; i++)
#define rep_e(c, s) for (auto c : s)

int main() {
    int n;
    cin >> n;
    vector<int> h(n + 1);
    h[0] = 0;
    for (int i = 0; i < n; i++) cin >> h[i + 1];
    int ans = 0;
    rep(i, 101) {
        rep(j, n) {
            if (h[j] < i && h[j + 1] >= i) ans++;
        }
    }
    cout << ans << "\n";
    return 0;
}