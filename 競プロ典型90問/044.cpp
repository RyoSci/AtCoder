// #define _GLIBCXX_DEBUG
#include <algorithm>
#include <atcoder/all>
#include <atcoder/modint>
#include <cmath>
#include <cstdio>
#include <deque>
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
    ll n, q;
    cin >> n >> q;
    vector<ll> a(n, 0);
    for (ll i = 0; i < n; i++) cin >> a[i];

    deque<ll> dq;
    rep(i, n) dq.emplace_back(a[i]);
    rep(i, q) {
        ll t, x, y;
        cin >> t >> x >> y;
        x--;
        y--;
        if (t == 1) {
            ll tmp = dq[x];
            dq[x] = dq[y];
            dq[y] = tmp;
        } else if (t == 2) {
            ll tmp = dq.back();
            dq.pop_back();
            dq.emplace_front(tmp);
        } else {
            cout << dq[x] << "\n";
        }
    }

    return 0;
}