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
    ll h, w, n;
    cin >> h >> w >> n;
    vector<ll> a(n, 0), b(n, 0);
    rep(i, n) cin >> a[i] >> b[i];

    set<ll> x, y;
    rep(i, n) {
        x.insert(a[i]);
        y.insert(b[i]);
    }

    vector<ll> xx, yy;
    rep_e(e, x) xx.emplace_back(e);
    rep_e(e, y) yy.emplace_back(e);

    rep(i, n) {
        ll nx = lower_bound(xx.begin(), xx.end(), a[i]) - xx.begin();
        ll ny = lower_bound(yy.begin(), yy.end(), b[i]) - yy.begin();
        cout << nx + 1 << ' ' << ny + 1 << "\n";
    }

    return 0;
}