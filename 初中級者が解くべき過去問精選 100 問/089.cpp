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

void chmax(ll &x, ll y) {
    if (x < y) x = y;
    return;
}

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];
    vector<ll> b;

    ll end = a[0];
    ll cnt = 1;
    rep_s(i, 1, n) {
        if (end != a[i]) {
            cnt++;
            end = a[i];
        } else {
            b.push_back(cnt);
            end = a[i];
            cnt = 1;
        }
    }
    if (cnt > 0) b.push_back(cnt);
    if (b.size() <= 2) {
        cout << n << "\n";
    } else {
        ll m = b.size();
        ll ans = 0;
        rep(i, m - 2) { chmax(ans, b[i] + b[i + 1] + b[i + 2]); }
        cout << ans << "\n";
    }

    return 0;
}