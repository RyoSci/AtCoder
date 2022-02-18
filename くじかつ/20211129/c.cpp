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
    string s;
    cin >> s;
    int k;
    cin >> k;
    int n = s.length();
    vector<int> dp(n + 1);
    rep(i, n) {
        if (s[i] == '.') dp[i + 1] += 1;
    }
    rep(i, n) { dp[i + 1] += dp[i]; }

    int ans = 0;
    int r = 0;
    rep(l, n) {
        while (r < n && dp[r + 1] - dp[l] <= k) r++;
        ans = max(ans, r - l);
    }
    cout << ans << "\n";
}