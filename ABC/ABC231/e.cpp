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
    ll n, x;
    cin >> n >> x;
    vector<ll> a(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    auto cal = [&](ll num) {
        ll cnt = 0;
        rep_r(i, n - 1, -1) {
            cnt += num / a[i];
            num %= a[i];
        }
        return cnt;
    };

    ll ans = x;
    ll tot = 0;
    rep_r(i, n - 1, -1) {
        // 超えた直後
        ll y;
        ll cnt;
        rep(j, n) {
            if (x > a[j]) continue;

            y = (x + a[j] - 1) / a[j] * a[j];
            cnt = cal(y) + cal(y - x) + tot;
            ans = min(ans, cnt);
        }

        // 超える直前
        y = x / a[i] * a[i];
        cnt = cal(y) + cal(x - y) + tot;
        ans = min(ans, cnt);
        tot += cal(y);
        x -= y;
    }

    cout << ans << "\n";

    return 0;
}