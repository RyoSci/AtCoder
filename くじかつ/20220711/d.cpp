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
    ll n, m;
    cin >> n >> m;
    vector<ll> a(n + 1);
    for (ll i = 0; i < n + 1; i++) cin >> a[i];
    vector<ll> c(n + m + 1);
    for (ll i = 0; i < n + m + 1; i++) cin >> c[i];

    reverse(a.begin(), a.end());
    reverse(c.begin(), c.end());

    vector<ll> b(m + 1, 0);

    rep(i, m + 1) {
        b[i] = c[i];
        rep(j, i) {
            if (i - j <= n) b[i] -= a[i - j] * b[j];
        }
        b[i] /= a[0];
    }
    reverse(b.begin(), b.end());
    for (auto a : b) cout << a << " ";
    cout << endl;

    return 0;
}