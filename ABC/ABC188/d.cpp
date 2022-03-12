// #define _GLIBCXX_DEBUG
#include <algorithm>
// #include <atcoder/all>
// #include <atcoder/modint>
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
// using namespace atcoder;
// using lli = long long;
// using mint = modint1000000007;
// using mint = modint998244353;
#define MOD 1000000007
#define INF (1L << 60)
#define EPS (1e-10)
typedef long long ll;
typedef pair<ll, ll> P;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n, c;
    cin >> n >> c;
    map<ll, ll> d;
    rep(i, n) {
        ll a, b, ci;
        cin >> a >> b >> ci;
        d[a] += ci;
        d[b + 1] -= ci;
    }
    ll key, val, pre_key, val_sum, ans;
    pre_key = 0;
    val_sum = 0;
    ans = 0;
    rep_e(i, d) {
        key = i.first;
        val = i.second;
        ans += (key - pre_key) * min(c, val_sum);
        pre_key = key;
        val_sum += val;
    }
    cout << ans << "\n";
    return 0;
}