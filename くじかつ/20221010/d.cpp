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
    ll n, m;
    cin >> n >> m;
    vector<vector<ll>> s(m);

    rep(i, m) {
        ll k;
        cin >> k;
        for (ll j = 0; j < k; j++) {
            ll sj;
            cin >> sj;
            sj--;
            s[i].emplace_back(sj);
        }
    }
    vector<ll> p(m);
    for (ll i = 0; i < m; i++) cin >> p[i];

    ll ans = 0;
    rep(sw, 1 << n) {
        ll on = 0;
        rep(i, m) {
            ll cnt = 0;
            rep_e(si, s[i]) {
                if (sw >> si & 1) cnt++;
            }
            if (cnt % 2 == p[i] % 2) on++;
        }

        if (on == m) ans++;
    }
    cout << ans << "\n";
    return 0;
}