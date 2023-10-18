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
    ll n, k;
    cin >> n >> k;
    vector<vector<ll>> t(n, vector<ll>(n, 0));
    rep(i, n) rep(j, n) cin >> t[i][j];
    vector<ll> a;
    rep(i, n - 1) a.emplace_back(i + 1);

    ll ans = 0;
    do {
        ll dis = 0;
        dis += t[0][a[0]];
        rep(i, n - 2) dis += t[a[i]][a[i + 1]];
        dis += t[a.back()][0];
        if (dis == k) ans++;
    } while (next_permutation(a.begin(), a.end()));

    cout << ans << "\n";
    return 0;
}