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
    ll n, c;
    cin >> n >> c;
    vector<vector<P>> channels(c);
    rep(i, n) {
        ll s, t, c;
        cin >> s >> t >> c;
        c--;
        channels[c].push_back(make_pair(s, t));
    }
    ll m = 1e5 + 10;
    vector<ll> cnt(m, 0);

    rep(i, c) {
        sort(channels[i].begin(), channels[i].end());
        ll pre = 0;
        rep_e(e, channels[i]) {
            // ll s, t;
            auto [s, t] = e;
            if (pre == s) s++;
            cnt[s]++;
            cnt[t + 1]--;
            pre = t;
        }
    }

    rep(i, m - 1) { cnt[i + 1] += cnt[i]; }
    ll ans = 0;
    rep(i, m) { ans = max(ans, cnt[i]); }

    cout << ans << "\n";
    return 0;
}