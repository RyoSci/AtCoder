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
    ll h, w;
    cin >> h >> w;
    vector<vector<ll>> a(h, vector<ll>(w, 0));
    rep(i, h) rep(j, w) { cin >> a[i][j]; }

    vector<tuple<ll, ll, ll, ll>> ans;
    rep(i, h) rep(j, w) {
        if (i == h - 1 && j == w - 1) continue;
        if (a[i][j] % 2 == 1) {
            if (j == w - 1) {
                a[i + 1][j] += 1;
                a[i][j] -= 1;
                ans.emplace_back(make_tuple(i + 1, j + 1, i + 2, j + 1));
            } else {
                a[i][j + 1] += 1;
                a[i][j] -= 1;
                ans.emplace_back(make_tuple(i + 1, j + 1, i + 1, j + 2));
            }
        }
    }
    cout << ans.size() << "\n";
    rep_e(i, ans) {
        auto [y, x, yy, xx] = i;
        cout << y << ' ' << x << ' ' << yy << ' ' << xx << "\n";
    }

    return 0;
}