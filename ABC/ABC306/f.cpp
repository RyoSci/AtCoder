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
    vector a(n, vector(m, 0ll));
    rep(i, n) rep(j, m) cin >> a[i][j];

    set<ll> st;
    ll l = n * m;
    map<ll, ll> mp;
    vector<ll> tot;
    rep(i, n) rep(j, m) tot.emplace_back(a[i][j]);
    sort(tot.begin(), tot.end());
    ll cnt = 0;
    fenwick_tree<ll> fw(l);
    rep_e(e, tot) {
        mp[e] = cnt;
        fw.add(cnt, 1);
        cnt++;
    }

    ll f = 0;
    rep(i, n) {
        rep(j, m) { fw.add(mp[a[i][j]], -1); }

        ll now = m * (m + 1) / 2 * (n - 1 - i);
        rep(j, m) { now += fw.sum(0, mp[a[i][j]] + 1); }
        f += now;
    }

    cout << f << "\n";

    return 0;
}