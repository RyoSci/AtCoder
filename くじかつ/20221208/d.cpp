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
    ll n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<string> b(m);
    for (ll i = 0; i < m; i++) cin >> b[i];

    bool ans = false;
    rep(si, n - m + 1) rep(sj, n - m + 1) {
        bool ok = true;
        rep(ti, m) rep(tj, m) {
            if (a[si + ti][sj + tj] != b[ti][tj]) ok = false;
        }
        if (ok) ans = true;
    }
    cout << (ans ? "Yes" : "No") << "\n";
    return 0;
}