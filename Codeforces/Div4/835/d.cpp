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
        vector<ll> b;

        ll now = a[0];
        rep(i, n - 1) {
            if (a[i] != a[i + 1]) {
                b.emplace_back(now);
                now = a[i + 1];
            }
        }
        b.emplace_back(now);

        ll m = b.size();
        ll cnt = 0;
        rep(i, m) {
            if (i == 0 or b[i - 1] > b[i]) {
                if (i == m - 1 or b[i] < b[i + 1]) cnt++;
            }
        }

        cout << (cnt == 1 ? "YES" : "NO") << "\n";
        // cout << cnt << "\n";
        // for (auto a : b) cout << a << " ";
        // cout << endl;
    }
    return 0;
}