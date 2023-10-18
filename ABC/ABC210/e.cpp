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
    ll n, m;
    cin >> n >> m;
    vector<ll> a(m, 0), c(m, 0);
    rep(i, m) cin >> a[i] >> c[i];

    auto gcd = [&](auto gcd, ll a, ll b) -> ll {
        if (b == 0) return a;
        return gcd(gcd, b, a % b);
    };

    vector<P> ac;
    rep(i, m) { ac.emplace_back(c[i], a[i]); }
    sort(ac.begin(), ac.end());
    ll cnt = n;
    ll ans = 0;
    rep(i, m) {
        auto [ci, ai] = ac[i];
        ll ncnt = gcd(gcd, cnt, ai);
        ans += (cnt - ncnt) * ci;
        cnt = ncnt;
    }
    if (cnt != 1) ans = -1;
    cout << ans << "\n";

    return 0;
}