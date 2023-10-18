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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n, c;
        cin >> n >> c;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        rep(i, n) c -= a[i] * a[i];

        ll ok = 0;
        ll ng = 1e9 + 10;

        while (ok + 1 < ng) {
            ll m = (ok + ng) / 2;

            ll cnt = 0;
            rep(i, n) { cnt += (a[i] + m + a[i]) * (a[i] + m - a[i]); }

            if (cnt <= c)
                ok = m;
            else
                ng = m;
        }

        cout << ok / 2 << "\n";
    }
    return 0;
}