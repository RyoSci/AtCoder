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
    int ans = 0;
    int n = s.length();

    rep(i, n) {
        rep(j, n) {
            string tmp = "";
            rep_s(k, i, j + 1) tmp += s[k];
            bool flag = true;
            for (char c : tmp) {
                if (c == 'A' | c == 'C' | c == 'G' | c == 'T')
                    continue;
                else
                    flag = false;
            }
            if (flag) ans = max(ans, j - i + 1);
        }
    }
    cout << ans << "\n";
    return 0;
}