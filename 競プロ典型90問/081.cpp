// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
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
using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
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
    ll n, k;
    cin >> n >> k;
    ll m = 5010;
    vector<vector<ll>> tot(m, vector<ll>(m, 0));
    rep(i, n) {
        ll a, b;
        cin >> a >> b;
        tot[a][b]++;
    }

    rep_s(i, 1, m) rep_s(j, 1, m) {
        tot[i][j] += tot[i - 1][j] + tot[i][j - 1] - tot[i - 1][j - 1];
    }

    // rep(i, m) {
    //     for (auto a : tot[i]) cout << a << " ";
    //     cout << endl;
    // }

    ll ans = 0;
    rep(top, m) {
        rep(right, m) {
            ll bot = max(top - k - 1, 0);
            ll left = max(right - k - 1, 0);
            ll res = tot[top][right] - tot[top][left] - tot[bot][right] +
                     tot[bot][left];
            ans = max(ans, res);
        }
    }
    cout << ans << "\n";
    return 0;
}