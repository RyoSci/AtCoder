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
        string s;
        cin >> s;
        ll x;
        cin >> x;
        vector<ll> t(1440, 0);
        ll hh = ((s[0] - '0') * 10 + (s[1] - '0')) * 60;
        ll mm = (s[3] - '0') * 10 + s[4] - '0';
        ll tmp = hh + mm;
        rep(i, 2000) {
            if (t[tmp] == 1) break;
            t[tmp] = 1;
            tmp += x;
            tmp %= 1440;
        }
        ll ans = 0;
        rep(i, 1440) {
            if (t[i] == 1) {
                ll h, m;
                h = i / 60;
                m = i % 60;
                if (h / 10 == m % 10 && h % 10 == m / 10) ans++;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}