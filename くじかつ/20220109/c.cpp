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

Int gcd(Int x, Int y) {
    if (y == 0) return x;
    return gcd(y, x % y);
}

int main() {
    Int n, m;
    cin >> n >> m;
    string s;
    cin >> s;
    string t;
    cin >> t;
    Int g = gcd(n, m);
    Int lcm = n * m / g;
    bool ans = true;

    rep(i, g) {
        if (s[i * lcm / m] == t[i * lcm / n])
            continue;
        else
            ans = false;
    }

    if (ans)
        cout << lcm << "\n";
    else
        cout << -1 << "\n";
    return 0;
}