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
    ll h, w, k;
    cin >> h >> w >> k;
    vector<string> s(h);
    for (ll i = 0; i < h; i++) cin >> s[i];

    ll ans = INF;
    rep(i, 1 << (h - 1)) {
        vector<ll> group(h, -1);
        ll id = 0;
        group[0] = id;
        rep(j, h - 1) {
            if (i >> j & 1) id++;
            group[j + 1] = id;
        }

        ll res = id;
        vector<ll> cnt(id + 1, 0);
        bool ok = true;
        rep(j, w) {
            rep(l, h) cnt[group[l]] += s[l][j] == '1';

            rep(l, id + 1) {
                if (cnt[l] > k) {
                    rep(m, id + 1) cnt[m] = 0;
                    res++;
                    rep(l, h) cnt[group[l]] += s[l][j] == '1';
                    break;
                }
            }
            rep(l, id + 1) {
                if (cnt[l] > k) ok = false;
            }
            if (!ok) break;
        }
        if (ok) ans = min(ans, res);
    }
    cout << ans << "\n";
    return 0;
}