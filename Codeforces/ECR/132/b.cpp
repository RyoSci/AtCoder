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
using lli = long long;
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
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> d(n + 1, 0), invd(n + 1, 0);
    rep(i, n - 1) { d[i + 1] = d[i] - min(0, a[i + 1] - a[i]); }
    rep_r(i, n - 1, 0) { invd[i - 1] = invd[i] - min(0, a[i - 1] - a[i]); }
    // invd[0] += invd[1];
    rep(i, m) {
        ll s, t;
        cin >> s >> t;
        ll ans;
        if (s < t) {
            ans = d[t - 1] - d[s - 1];
        } else {
            ans = invd[t - 1] - invd[s - 1];
        }
        cout << ans << "\n";
    }
    // for (auto a : d) cout << a << " ";
    // cout << endl;
    // for (auto a : invd) cout << a << " ";
    // cout << endl;
    return 0;
}