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
    ll h, w;
    cin >> h >> w;
    vector<vector<ll>> a(h, vector<ll>(w, 0));
    rep(i, h) rep(j, w) cin >> a[i][j];

    vector<ll> tate(h, 0), yoko(w, 0);
    rep(i, h) {
        rep(j, w) {
            tate[i] += a[i][j];
            yoko[j] += a[i][j];
        }
    }

    vector<vector<ll>> b(h, vector<ll>(w, 0));
    rep(i, h) rep(j, w) b[i][j] = tate[i] + yoko[j] - a[i][j];

    rep(i, h) for (auto a : b[i]) cout << a << " ";
    cout << endl;
    return 0;
}