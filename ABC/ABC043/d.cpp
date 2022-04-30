// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    string s;
    cin >> s;
    vector<vector<ll>> pos(26);
    ll n = s.size();
    rep(i, n) {
        ll tmp = s[i] - 'a';
        pos[tmp].emplace_back(i);
    }

    ll a = -1, b = -1;
    rep(i, 26) {
        ll m = pos[i].size();
        if (m < 2) continue;
        rep(j, m - 1) {
            if (pos[i][j + 1] - pos[i][j] <= 2) {
                a = pos[i][j] + 1, b = pos[i][j + 1] + 1;
                // cout << a << ' ' << b << "\n";
            }
        }
    }
    cout << a << ' ' << b << "\n";

    return 0;
}