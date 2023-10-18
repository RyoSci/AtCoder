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

    vector<ll> a(m), b(m);
    rep(i, m) cin >> a[i] >> b[i];

    vector<ll> ans;

    ll now = n * (n - 1) / 2;
    dsu uf(n);

    rep_r(i, m - 1, -1) {
        ans.emplace_back(now);
        if (uf.same(a[i] - 1, b[i] - 1)) continue;
        now -= uf.size(a[i] - 1) * uf.size(b[i] - 1);
        uf.merge(a[i] - 1, b[i] - 1);
    }

    reverse(ans.begin(), ans.end());
    for (auto a : ans) cout << a << " ";
    cout << endl;
    return 0;
}