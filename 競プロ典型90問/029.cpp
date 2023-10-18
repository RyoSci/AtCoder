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
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
typedef tuple<ll, ll, ll> T;
// #define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

using S = long long;
using F = long long;

const S INF = 8e18;
const F ID = 8e18;

S op(S a, S b) { return std::max(a, b); }
S e() { return -INF; }
S mapping(F f, S x) { return (f == ID ? x : f); }
F composition(F f, F g) { return (f == ID ? g : f); }
F id() { return ID; }

int main() {
    ll w, n;
    cin >> w >> n;

    std::vector<S> v(w + 1);
    atcoder::lazy_segtree<S, op, e, F, mapping, composition, id> seg(v);
    rep(i, n) {
        ll l, r;
        cin >> l >> r;
        ll h = seg.prod(l, r + 1);
        cout << h + 1 << "\n";
        seg.apply(l, r + 1, h + 1);
    }
}