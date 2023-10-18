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
    vector<vector<ll>> c(3, vector<ll>(3, 0));
    rep(i, 3) rep(j, 3) cin >> c[i][j];

    ll a1 = 0;
    vector<ll> b(3, 0);
    rep(i, 3) b[i] = c[0][i] - a1;
    vector<set<ll>> a(3);
    rep(i, 3) rep(j, 3) a[i].insert(c[i][j] - b[j]);

    bool ans = true;
    rep(i, 3) if (a[i].size() > 1) ans = false;

    cout << (ans ? "Yes" : "No") << "\n";
    return 0;
}