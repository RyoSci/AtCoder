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
// using mint = modint998244353;
using mint = modint;
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
    ll n, p;
    cin >> n >> p;
    string s;
    cin >> s;
    reverse(s.begin(), s.end());
    if (p == 2 or p == 5) {
        ll ans = 0;
        rep(i, n) {
            ll now = s[i] - '0';
            if (now % p == 0) ans += n - i;
        }
        cout << ans << "\n";
        return 0;
    }
    modint::set_mod(p);
    vector<mint> mod(n + 1, 0);
    rep(i, n) {
        ll now = s[i] - '0';
        // mod[i + 1] = mod[i] * 10 + now;
        mod[i + 1] = now * mint(10).pow(i) + mod[i];
    }

    map<ll, ll> d;
    ll ans = 0;
    rep(i, n + 1) {
        ans += d[mod[i].val()];
        d[mod[i].val()]++;
    }

    cout << ans << "\n";

    return 0;
}