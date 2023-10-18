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
    ll n, a, b;
    cin >> n >> a >> b;
    ll p, q, r, s;
    cin >> p >> q >> r >> s;

    ll h = q - p + 1;
    ll w = s - r + 1;
    vector<vector<char>> g(h, vector<char>(w, '.'));

    rep(i, h) rep(j, w) {
        ll ni = i + p;
        ll nj = j + r;
        ll ki = ni - a;
        ll kj = nj - b;
        if (ki == kj and max(1 - a, 1 - b) <= ki and ki <= min(n - a, n - b))
            g[i][j] = '#';
        ki = ni - a;
        kj = -nj + b;
        if (ki == kj and max(1 - a, b - n) <= ki and ki <= min(n - a, b - 1))
            g[i][j] = '#';
    }

    rep(i, h) {
        for (auto a : g[i]) cout << a << "";
        cout << endl;
    }

    return 0;
}