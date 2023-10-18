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
    ll n, p, q, r;
    cin >> n >> p >> q >> r;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> tot(n + 1, 0);
    rep(i, n) tot[i + 1] = tot[i] + a[i];
    tot.emplace_back(INF);
    bool ans = false;
    rep_s(i, 0, n + 1) {
        ll ni = i;
        auto iter = lower_bound(tot.begin(), tot.end(), tot[ni] + p);
        ll tmp = *iter - tot[ni];
        if (tmp != p) continue;
        ni = iter - tot.begin();
        iter = lower_bound(tot.begin(), tot.end(), tot[ni] + q);
        tmp = *iter - tot[ni];
        if (tmp != q) continue;
        ni = iter - tot.begin();
        iter = lower_bound(tot.begin(), tot.end(), tot[ni] + r);
        tmp = *iter - tot[ni];
        if (tmp != r) continue;
        ans = true;
    }
    cout << (ans ? "Yes" : "No") << "\n";
    return 0;
}