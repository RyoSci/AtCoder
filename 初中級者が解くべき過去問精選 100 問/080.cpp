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
    ll h, w, K, V;
    cin >> h >> w >> K >> V;
    vector<vector<ll>> a(h + 1, vector<ll>(w + 1, 0));
    rep(i, h) {
        rep(j, w) { cin >> a[i + 1][j + 1]; }
    }

    rep(i, h) {
        rep(j, w) { a[i + 1][j + 1] += a[i + 1][j] + a[i][j + 1] - a[i][j]; }
    }

    ll ans = 0;
    ll tmp, area;
    rep(i, h + 1) {
        rep_s(j, i, h + 1) {
            rep(k, w + 1) {
                rep_s(l, k, w + 1) {
                    tmp = a[j][l] - a[j][k] - a[i][l] + a[i][k];
                    area = (j - i) * (l - k);
                    tmp += area * K;
                    if (tmp <= V) ans = max(ans, area);
                }
            }
        }
    }
    cout << ans << "\n";
    return 0;
}