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

map<ll, ll> div_ele(ll m) {
    map<ll, ll> res;
    ll now = m;
    for (ll i = 2; i * i <= m; i++) {
        while (true) {
            if (now % i == 0) {
                res[i]++;
                now /= i;
            } else
                break;
        }
    }
    if (now != 1) res[now]++;
    return res;
}

vector<mint> fac(1e5 + 200);
vector<mint> inv(1e5 + 200);
vector<mint> invfac(1e5 + 200);

mint cal(ll n, ll k) {
    if (n < k | k < 0 | n < 0) return mint(0);
    mint ans = fac[n] * invfac[n - k] * invfac[k];
    return ans;
}

int main() {
    ll n, m;
    cin >> n >> m;

    map<ll, ll> res = div_ele(m);

    mint ans = mint(1);
    fac[0] = mint(1);
    invfac[0] = mint(1);
    rep_s(i, 1, 1e5 + 100) { fac[i] = i * fac[i - 1]; }
    rep_s(i, 1, 1e5 + 100) { inv[i] = mint(1) / i; }
    rep_s(i, 1, 1e5 + 100) { invfac[i] = invfac[i - 1] * inv[i]; }

    auto begin = res.begin(), end = res.end();
    for (auto iter = begin; iter != end; iter++) {
        // first: key, second: value
        ll key = iter->first;
        ll val = iter->second;
        ans *= cal(val + n - 1, val);
    }
    cout << ans.val() << "\n";

    return 0;
}