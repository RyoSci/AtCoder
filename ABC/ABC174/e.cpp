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

ll n, k;
vector<ll> a;

ll f(ll x) {
    ll cnt = 0;
    rep(i, n) { cnt += (a[i] + x - 1) / x - 1; }
    return cnt;
}

int main() {
    cin >> n >> k;
    a.resize(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    ll ng = 0;
    ll ok = INF;
    while (ng + 1 < ok) {
        ll m = (ng + ok) / 2;
        if (f(m) <= k)
            ok = m;
        else
            ng = m;
    }
    cout << ok << "\n";

    return 0;
}