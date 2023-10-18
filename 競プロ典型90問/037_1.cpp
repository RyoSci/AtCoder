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
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

using S = long long;
using F = long long;

const S INF = 8e18;
const F ID = 8e18;

S op(S a, S b) { return max(a, b); }
S e() { return -INF; }
S mapping(F f, S x) { return (f == ID ? x : f); }
F composition(F f, F g) { return (f == ID ? g : f); }
F id() { return ID; }

int main() {
    ll w, n;
    cin >> w >> n;

    vector<S> v(w + 1, -INF);
    v[0] = 0;
    lazy_segtree<S, op, e, F, mapping, composition, id> seg(v);

    vector<ll> l(n), r(n), vals(n);
    for (ll i = 0; i < n; i++) cin >> l[i] >> r[i] >> vals[i];

    rep(i, n) {
        rep_r(j, w, -1) {
            if (0 <= j - l[i]) {
                // ll now = seg.get(j);
                // seg.apply(j + l[i], min(w, j + r[i]) + 1, now + vals[i]);
                ll now = seg.prod(max(0, j - r[i]), j - l[i] + 1);
                if (now == -INF) continue;
                ll pre = seg.get(j);
                ll nxt = now + vals[i];
                if (pre < nxt) seg.set(j, now + vals[i]);
                // cout << now << ' ' << i << " " << j << "\n";
                // rep(i, w + 1) cout << seg.get(i) << " ";
                // cout << "\n";
            }
        }
    }

    if (seg.get(w) == -INF)
        cout << -1 << "\n";
    else
        cout << seg.get(w) << "\n";

    return 0;
}