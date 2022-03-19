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
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<P> b;
    ll pre = a[0];
    ll now = 0;
    rep(i, n) {
        if (pre == a[i])
            now++;
        else {
            b.push_back(make_pair(pre, now));
            now = 1;
        }
        pre = a[i];
    }
    b.push_back(make_pair(pre, now));

    ll cnt = 0;
    rep(i, n) {
        if (a[i]) cnt++;
    }

    ll ans_max = cnt;
    ll ans_min = cnt;

    b.push_back(make_pair(2, 0));

    ll c = cnt;
    rep(i, b.size() - 1) {
        ll z_or_o, now, n_z_or_o, next;
        tie(z_or_o, now) = b[i];
        tie(n_z_or_o, next) = b[i + 1];
        if (!z_or_o) {
            c += now;
            ans_max = max(ans_max, c);
            c -= next;
            if (c < cnt) c = cnt;
        }
    }

    c = cnt;
    rep(i, b.size() - 1) {
        ll z_or_o, now, n_z_or_o, next;
        tie(z_or_o, now) = b[i];
        tie(n_z_or_o, next) = b[i + 1];
        if (z_or_o) {
            c -= now;
            ans_min = min(ans_min, c);
            c += next;
            if (c > cnt) c = cnt;
        }
    }

    cout << ans_max - ans_min + 1 << "\n";
    return 0;
}