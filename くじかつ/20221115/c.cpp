// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
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
using namespace atcoder;
using lli = long long;
// using mint = modint1000000007;
using mint = modint998244353;
// #define MOD 1000000007
#define MOD 998244353
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    vector<string> s(9);
    rep(i, 9) cin >> s[i];

    ll res = 0;
    rep(a, 9) rep(b, 9) {
        if (s[a][b] == '.') continue;
        rep(c, 9) rep(d, 9) {
            if (s[c][d] == '.') continue;

            if (a == c and b == d) continue;

            ll dx = c - a;
            ll dy = d - b;

            ll nc = c + dy;
            ll nd = d - dx;
            ll na = a + dy;
            ll nb = b - dx;
            if (0 <= na and na < 9 and 0 <= nb and nb < 9 and
                s[na][nb] == '#') {
                if (0 <= nc and nc < 9 and 0 <= nd and nd < 9 and
                    s[nc][nd] == '#') {
                    res++;
                    // cout << a << ' ' << b << ' ' << c << ' ' << d << "\n";
                }
            }
        }
    }

    cout << res / 4 << "\n";
    return 0;
}