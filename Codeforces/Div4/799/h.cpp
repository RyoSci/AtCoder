// #define _GLIBCXX_DEBUG
#include <algorithm>
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
    rep(_, t) {
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        map<ll, vector<ll>> d;
        rep(i, n) { d[a[i]].push_back(i); }

        ll ans = 0;
        ll ans_a = a[0];
        ll ans_l = 1;
        ll ans_r = 1;
        rep_e(e, d) {
            auto [key, vals] = e;
            vector<ll> tot(vals.size() + 1, 0);
            rep(i, vals.size()) {
                ll other = vals[i] - i;
                tot[i] = i + 1 - other;
            }
            ll tmp = INF;
            ll tmp_l = 0;
            rep(i, vals.size()) {
                if (tmp > tot[i]) {
                    tmp = tot[i];
                    tmp_l = i;
                }
                if (ans < tot[i] - tmp) {
                    ans = tot[i] - tmp;
                    ans_a = key;
                    ans_l = vals[tmp_l] + 1;
                    ans_r = vals[i] + 1;
                }
            }
        }
        cout << ans_a << ' ' << ans_l << ' ' << ans_r << "\n";
    }
    return 0;
}