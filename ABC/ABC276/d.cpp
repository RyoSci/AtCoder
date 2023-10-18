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
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    map<ll, vector<ll>> d;
    rep(i, n) {
        ll ai = a[i];
        ll cnt = 0;
        vector<P> q;
        q.emplace_back(P(ai, cnt));
        map<ll, ll> tmp_d;
        while (q.size() > 0) {
            auto [ai, cnt] = q.back();
            q.pop_back();
            if (tmp_d[ai] == 0)
                tmp_d[ai] = cnt;
            else
                tmp_d[ai] = min(tmp_d[ai], cnt);

            if (ai % 2 == 0) q.emplace_back(P(ai / 2, cnt + 1));
            if (ai % 3 == 0) q.emplace_back(P(ai / 3, cnt + 1));
        }

        rep_e(e, tmp_d) {
            auto [key, val] = e;
            d[key].emplace_back(val);
        }
    }

    ll ans = INF;
    rep_e(e, d) {
        auto [key, vals] = e;
        if (vals.size() == n) {
            ll res = 0;
            rep_e(val, vals) res += val;
            ans = min(ans, res);
        }
    }
    if (ans == INF)
        cout << -1 << "\n";
    else
        cout << ans << "\n";
    return 0;
}