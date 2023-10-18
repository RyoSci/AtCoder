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
    ll n;
    cin >> n;
    vector<ll> p(n);
    for (ll i = 0; i < n; i++) cin >> p[i];
    ll ans = INF;
    ll now = 0;
    rep(i, n) now += min((p[i] + n - i) % n, (i + n - p[i]) % n);

    ll up_now = 0, down_now = 0, equal_now = 0;
    vector<ll> up_time(n, 0), down_time(n, 0), equal_time(n, 0);
    rep(i, n) {
        ll dis = (p[i] + n - i) % n;
        up_time[dis]++;
        if (n % 2 == 1) {
            equal_time[(dis + n / 2) % n]++;
            down_time[(dis + n / 2 + 1) % n]++;
            if (0 < dis and dis <= n / 2)
                down_now++;
            else if (dis == n / 2 + 1)
                equal_now++;
            else
                up_now++;
        } else {
            down_time[(dis + n / 2) % n]++;
            if (0 < dis and dis <= n / 2)
                down_now++;
            else
                up_now++;
        }
    }

    // for (auto a : up_time) cout << a << " ";
    // cout << endl;
    // for (auto a : down_time) cout << a << " ";
    // cout << endl;
    // for (auto a : equal_time) cout << a << " ";
    // cout << endl;

    ans = min(ans, now);

    // cout << now << "\n";
    // cout << up_now << ' ' << down_now << ' ' << equal_now << "\n";

    rep_s(i, 1, n) {
        now += up_now - down_now;
        if (n % 2 == 1) {
            up_now += up_time[i];
            down_now -= up_time[i];
            equal_now += equal_time[i];
            up_now -= equal_time[i];
            down_now += down_time[i];
            equal_now -= down_time[i];
        } else {
            up_now += up_time[i];
            down_now -= up_time[i];
            down_now += down_time[i];
            up_now -= down_time[i];
        }
        // cout << i << ' ' << up_now << ' ' << down_now << ' ' << now << ' '
        //      << ans << "\n";
        ans = min(ans, now);
    }
    now += up_now - down_now;
    ans = min(ans, now);

    cout << ans << "\n";

    return 0;
}