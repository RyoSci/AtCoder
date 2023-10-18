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
    ll n, q;
    cin >> n >> q;

    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> b(n - 1, 0);
    ll now = 0;
    rep(i, n - 1) {
        b[i] = a[i + 1] - a[i];
        now += abs(b[i]);
    }

    rep(i, q) {
        ll l, r, v;
        cin >> l >> r >> v;
        l--;
        r--;
        if (0 < l) {
            ll tmp = b[l - 1];
            b[l - 1] += v;
            now -= abs(tmp);
            now += abs(b[l - 1]);
        }
        if (r < n - 1) {
            ll tmp = b[r];
            b[r] -= v;
            now -= abs(tmp);
            now += abs(b[r]);
        }
        cout << now << "\n";
    }

    return 0;
}