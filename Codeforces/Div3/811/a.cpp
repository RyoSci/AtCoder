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
using lli = long long;
// using mint = modint1000000007;
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
    ll t;
    cin >> t;
    vector<P> ans;

    rep(_, t) {
        ll n, h, m;
        cin >> n >> h >> m;
        vector<ll> a;
        rep(i, n) {
            ll hh, mm;
            cin >> hh >> mm;
            a.push_back(hh * 60 + mm);
            a.push_back(hh * 60 + 24 * 60 + mm);
        }
        sort(a.begin(), a.end());
        auto iter = lower_bound(a.begin(), a.end(), h * 60 + m);
        ll dis = *iter - (h * 60 + m);
        ll hh = dis / 60;
        ll mm = dis % 60;
        // cout << hh << ' ' << mm << "\n";
        ans.emplace_back(make_pair(hh, mm));
    }
    rep(i, t) cout << ans[i].first << ' ' << ans[i].second << "\n";
    return 0;
}