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
#define INF (1LL << 60)
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
    ll n;
    cin >> n;
    vector<ll> x(n, 0), y(n, 0), h(n, 0);
    rep(i, n) cin >> x[i] >> y[i] >> h[i];

    rep(cx, 101) {
        rep(cy, 101) {
            bool ok = true;
            set<ll> HS;
            rep(i, n) {
                if (h[i] > 0) {
                    ll H = h[i] + abs(x[i] - cx) + abs(y[i] - cy);
                    HS.insert(H);
                }
            }
            if (HS.size() != 1) continue;
            ll H = *HS.begin();
            rep(i, n) {
                if (h[i] == 0) {
                    ll tmp = H - abs(x[i] - cx) - abs(y[i] - cy);
                    if (tmp > 0) ok = false;
                }
            }
            if (ok) {
                cout << cx << ' ' << cy << ' ' << H << "\n";
                return 0;
            }
        }
    }
    return 0;
}