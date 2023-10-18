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
    ll n;
    cin >> n;
    vector<ll> a(n), b(n);
    rep(i, n) cin >> a[i] >> b[i];

    map<ll, ll> tot;
    tot[0] = 0;
    rep(i, n) {
        tot[a[i]]++;
        tot[a[i] + b[i]]--;
    }

    ll pre = 0;
    for (auto [key, val] : tot) {
        tot[key] += pre;
        pre = tot[key];
    }

    ll pre_key = 0;
    ll pre_val = 0;
    vector<ll> ans(n + 1, 0);

    for (auto [key, val] : tot) {
        ans[pre_val] += key - pre_key;
        pre_key = key;
        pre_val = val;
    }

    rep(i, n) cout << ans[i + 1] << "\n";

    return 0;
}