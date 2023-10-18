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
#define INF (1LL << 60)
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

    vector a(2 * n, vector(2 * n + 1, -1ll));

    rep(i, 2 * n - 1) {
        for (ll j = i + 1; j < 2 * n; j++) cin >> a[i][j];
    }

    // rep(i, 2 * n) {
    //     for (auto a : a[i]) cout << a << " ";
    //     cout << endl;
    // }

    ll ans = -INF;

    auto dfs = [&](auto dfs, ll i, ll mask, ll res, ll pre) {
        if (i == 2 * n) {
            ans = max(ans, res);
            return;
        }
        if (i % 2 == 0) {
            rep_s(j, 0, 2 * n) {
                if (!(mask >> j & 1)) {
                    mask |= (1 << j);
                    dfs(dfs, i + 1, mask, res, j);
                    mask ^= (1 << j);
                    break;
                }
            }
        } else {
            rep_s(j, pre + 1, 2 * n) {
                if (!(mask >> j & 1)) {
                    ll tmp = res;
                    res ^= a[pre][j];
                    mask |= (1 << j);
                    dfs(dfs, i + 1, mask, res, j);
                    res = tmp;
                    mask ^= (1 << j);
                }
            }
        }
    };

    dfs(dfs, 0, 0, 0, -1);

    cout << ans << "\n";
    return 0;
}