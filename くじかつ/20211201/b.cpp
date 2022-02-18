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

int cal(int x) {
    int res = 0;
    while (x > 1) {
        if (x % 2 == 0)
            x /= 2;
        else
            break;
        res++;
    }
    return res;
}

int main() {
    int n;
    cin >> n;
    int ans = 1;
    rep_s(i, 1, n + 1) {
        if (cal(ans) < cal(i)) ans = i;
    }
    cout << ans << "\n";
    return 0;
}