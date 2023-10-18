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
    ll h, w;
    cin >> h >> w;
    vector<vector<ll>> p(h, vector<ll>(w));
    rep(i, h) rep(j, w) cin >> p[i][j];

    ll ans = 0;
    rep_s(i, 1, 1 << h) {
        vector<ll> tmp;
        rep(j, h) {
            if (!(i >> j & 1)) continue;
            tmp.emplace_back(j);
        }

        map<ll, ll> d;
        rep(j, w) {
            bool ok = true;
            rep(k, tmp.size() - 1) {
                if (p[tmp[k]][j] != p[tmp[k + 1]][j]) ok = false;
            }
            if (ok) d[p[tmp[0]][j]]++;
        }
        ll cnt = 0;
        for (auto [key, val] : d) {
            cnt = max(cnt, val);
        }
        ans = max(ans, tmp.size() * cnt);
    }
    cout << ans << "\n";
    return 0;
}