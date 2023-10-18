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
    ll n;
    cin >> n;
    vector<vector<ll>> a(n, vector<ll>(n, 0));
    rep(i, n) rep(j, n) cin >> a[i][j];
    ll m;
    cin >> m;

    vector<vector<ll>> xy(11, vector<ll>(11, 0));

    rep(i, m) {
        ll x, y;
        cin >> x >> y;
        x--;
        y--;
        xy[x][y] = 1;
        xy[y][x] = 1;
    }

    vector<ll> nums(n);
    rep(i, n) nums[i] = i;
    ll ans = INF;
    do {
        ll tmp = 0;
        rep(i, n - 1) {
            ll j = nums[i];
            tmp += a[j][i];
            if (xy[nums[i]][nums[i + 1]]) tmp = INF;
        }
        ll j = nums[n - 1];
        tmp += a[j][n - 1];
        ans = min(ans, tmp);

    } while (next_permutation(nums.begin(), nums.end()));

    if (ans == INF)
        cout << -1 << "\n";
    else
        cout << ans << "\n";

    return 0;
}