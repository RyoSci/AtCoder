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
    ll n, k, q;
    cin >> n >> k >> q;
    vector<ll> a(k + 1);
    for (ll i = 0; i < k; i++) cin >> a[i];
    a[k] = n + 1;
    vector<ll> l(q);
    for (ll i = 0; i < q; i++) cin >> l[i];

    rep(i, q) {
        if (a[l[i] - 1] + 1 != a[l[i]]) a[l[i] - 1]++;
    }

    rep(i, k) cout << a[i] << "\n";
    return 0;
}