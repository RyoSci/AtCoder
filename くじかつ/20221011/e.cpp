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

ll n, k;
vector<ll> a(100000);

ll f(ll x) {
    ll cnt = 0;
    rep(i, n) { cnt += min(a[i], x); }
    return cnt;
}

int main() {
    cin >> n >> k;
    a.resize(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    ll low_k = 0;
    ll up_k = INF;

    while (low_k + 1 < up_k) {
        ll m = (low_k + up_k) / 2;
        if (f(m) < k)
            low_k = m;
        else
            up_k = m;
    }

    k -= f(low_k);
    rep(i, n) { a[i] = max(a[i] - low_k, 0); }

    rep(i, n) {
        if (k == 0) break;
        if (a[i] > 0) {
            a[i]--;
            k--;
        }
    }

    for (auto a : a) cout << a << " ";
    cout << endl;
    return 0;
}