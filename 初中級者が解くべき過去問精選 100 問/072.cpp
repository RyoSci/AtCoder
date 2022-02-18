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
#define INF (1 << 29)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)
#define _GLIBCXX_DEBUG

mint comb(ll n, ll k) {
    mint res = 1;
    rep_r(i, n, n - k) { res = res * i; }
    rep_r(i, k, 0) { res = res * mint(i).pow(MOD - 2); }
    return res;
}

int main() {
    ll w, h;
    cin >> w >> h;
    w--;
    h--;
    // w+hCwを計算したい
    if (w > h) swap(w, h);
    cout << comb(w + h, w).val() << "\n";

    return 0;
}