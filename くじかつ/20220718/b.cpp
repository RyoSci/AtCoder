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
    ll n;
    cin >> n;
    vector<double> t(n), l(n), r(n);
    for (ll i = 0; i < n; i++) {
        cin >> t[i] >> l[i] >> r[i];
        if (t[i] == 2) {
            r[i] -= 0.5;
        } else if (t[i] == 3) {
            l[i] += 0.5;
        } else if (t[i] == 4) {
            r[i] -= 0.5;
            l[i] += 0.5;
        }
    }

    ll ans = 0;
    rep(i, n - 1) rep_s(j, i + 1, n) {
        if (!(r[i] < l[j] | r[j] < l[i])) ans++;
    }

    cout << ans << "\n";
    return 0;
}