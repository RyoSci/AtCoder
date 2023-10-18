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
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
using namespace atcoder;
using lli = long long;
// using mint = modint1000000007;
using mint = modint998244353;
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
    ll n, m;
    cin >> n >> m;
    ll a, b, c, d, e, f;
    cin >> a >> b >> c >> d >> e >> f;
    vector<ll> ace = {a, c, e};
    vector<ll> bdf = {b, d, f};

    // set<P> NG;
    unordered_set<P> NG;
    rep(i, m) {
        ll xi, yi;
        cin >> xi >> yi;
        NG.insert({xi, yi});
    }

    map<P, mint> pre;
    // unordered_map<P, mint> pre;
    pre[{0, 0}] = 1;
    rep(i, n) {
        map<P, mint> nxt;
        // unordered_map<P, mint> nxt;
        rep_e(e, pre) {
            auto [xy, cnt] = e;
            ll x = xy.first;
            ll y = xy.second;
            rep(j, 3) {
                ll nx = x + ace[j];
                ll ny = y + bdf[j];
                P tmp;
                tmp.first = nx;
                tmp.second = ny;
                if (NG.count(tmp) == 0) {
                    nxt[tmp] += cnt;
                }
            }
        }
        pre = nxt;
        // swap(pre, nxt);
    }

    mint ans = 0;
    rep_e(e, pre) {
        auto [xy, cnt] = e;
        ans += cnt;
    }

    cout << ans.val() << "\n";

    return 0;
}