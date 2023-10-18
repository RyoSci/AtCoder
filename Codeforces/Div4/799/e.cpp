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
typedef tuple<ll, ll, ll> T;
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll t;
    cin >> t;
    rep(_, t) {
        ll n, s;
        cin >> n >> s;
        vector<ll> a(n + 1);
        for (ll i = 1; i < n + 1; i++) cin >> a[i];
        ll cnt = 0;
        rep(i, n + 1) if (a[i] == 1) cnt++;
        if (cnt < s) {
            cout << -1 << "\n";
            continue;
        }
        rep(i, n) a[i + 1] += a[i];
        ll ans = -1;
        rep(i, n + 1) {
            ll tmp = a[i] + s;
            auto iter = upper_bound(a.begin(), a.end(), tmp);
            iter--;
            if (*iter != tmp) continue;
            ans = max(ans, iter - a.begin() - i);
        }
        cout << n - ans << "\n";
    }
    return 0;
}