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
    ll n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> f(n);
    for (ll i = 0; i < n; i++) cin >> f[i];

    sort(a.rbegin(), a.rend());
    sort(f.begin(), f.end());

    auto cal = [&](ll x) {
        ll use = 0;
        rep(i, n) { use += max(0, a[i] - x / f[i]); }
        return use <= k;
    };
    ll ok = INF;
    ll ng = -1;
    while (ng + 1 < ok) {
        ll m = (ng + ok) / 2;
        if (cal(m))
            ok = m;
        else
            ng = m;
    }
    cout << ok << "\n";
    return 0;
}