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
    Int n, s;
    cin >> n >> s;
    vector<Int> a(n), b(n);
    rep(i, n) { cin >> a[i] >> b[i]; }
    vector<vector<Int>> dp(n + 1, vector<Int>(s + 1));
    //  dp[i][j]<=i番目まで福袋を購入した際にj円になる購入の仕方があるかないか
    dp[0][0] = 1;
    rep(i, n) {
        rep(j, s) {
            if (dp[i][j] == 0) continue;
            if (j + a[i] <= s) dp[i + 1][j + a[i]] = 1;
            if (j + b[i] <= s) dp[i + 1][j + b[i]] = 1;
        }
    }
    if (dp[n][s] == 0)
        cout << "Impossible"
             << "\n";
    else {
        vector<char> ans;
        Int j = s;
        rep_r(i, n, 0) {
            if (j - a[i - 1] >= 0 && dp[i - 1][j - a[i - 1]] == 1) {
                j -= a[i - 1];
                ans.push_back('A');
            } else if (j - b[i - 1] >= 0 && dp[i - 1][j - b[i - 1]] == 1) {
                j -= b[i - 1];
                ans.push_back('B');
            }
        }
        reverse(ans.begin(), ans.end());
        for (char a : ans) cout << a << "";
    }

    return 0;
}