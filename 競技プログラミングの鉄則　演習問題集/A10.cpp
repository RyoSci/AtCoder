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
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> from_l(n + 1), from_r(n + 1);

    auto chmax = [&](ll &x, ll y) {
        if (x < y) x = y;
        return;
    };

    rep(i, n) {
        chmax(from_l[i + 1], from_l[i]);
        chmax(from_l[i + 1], a[i]);
    }
    rep_r(i, n - 1, -1) {
        chmax(from_r[i], from_r[i + 1]);
        chmax(from_r[i], a[i]);
    }

    ll d;
    cin >> d;
    rep(i, d) {
        ll l, r;
        cin >> l >> r;
        ll ans = max(from_l[l - 1], from_r[r]);
        cout << ans << "\n";
    }

    return 0;
}