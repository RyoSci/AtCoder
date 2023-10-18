// #define _GLIBCXX_DEBUG
#include <algorithm>
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
using lli = long long;
// #define MOD 1000000007
#define MOD 998244353
#define INF 1001001
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
        ll l, r, x;
        cin >> l >> r >> x;
        ll a, b;
        cin >> a >> b;
        if (a == b) {
            cout << 0 << "\n";
        } else if (abs(b - a) >= x) {
            cout << 1 << "\n";
        } else {
            ll ans = INF;
            ll tmp = 0;
            if (a + x <= r) {
                // rに行く
                tmp++;
                // rからbに行けるなら
                if (r - b >= x) ans = min(ans, tmp + 1);
                // rからlに行けるなら
                if (l <= r - x) {
                    tmp++;
                    // lからbに行けるなら
                    if (b - l >= x) ans = min(ans, tmp + 1);
                }
            }
            tmp = 0;
            if (l <= a - x) {
                tmp++;
                if (b - l >= x) ans = min(ans, tmp + 1);
                if (l + x <= r) {
                    tmp++;
                    if (r - b >= x) ans = min(ans, tmp + 1);
                }
            }
            if (ans == INF)
                cout << -1 << "\n";
            else
                cout << ans << "\n";
        }
    }
    return 0;
}