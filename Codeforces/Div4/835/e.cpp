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
    ll t;
    cin >> t;
    rep(_, t) {
        ll n;
        cin >> n;
        vector<ll> a(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        ll z = 0;
        ll ans = 0;
        rep_r(i, n - 1, -1) {
            if (a[i] == 1) {
                ans += z;
            } else
                z++;
        }
        vector<ll> cnt(2, 0);
        cnt[0] = z;
        ll tmp = ans;
        rep(i, n) {
            if (a[i] == 1) {
                ans = max(ans, tmp + cnt[1] - cnt[0]);
                cnt[1]++;
            } else {
                cnt[0]--;
                ans = max(ans, tmp + cnt[0] - cnt[1]);
            }
        }
        cout << ans << "\n";
    }
    return 0;
}