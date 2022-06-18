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
    vector<ll> a(3 * n);
    for (ll i = 0; i < 3 * n; i++) cin >> a[i];
    vector<ll> l(n + 1, 0);
    vector<ll> r(n + 1, 0);
    priority_queue<ll> q;
    ll sum_l = 0;
    rep(i, n) {
        q.push(-a[i]);
        sum_l += a[i];
    }
    l[0] = sum_l;

    rep_s(i, 1, n + 1) {
        ll tmp = -q.top();
        q.pop();
        if (tmp < a[n - 1 + i]) {
            q.push(-a[n - 1 + i]);
            sum_l -= tmp;
            sum_l += a[n - 1 + i];
        } else {
            q.push(-tmp);
        }
        l[i] = sum_l;
    }

    priority_queue<ll> qq;
    ll sum_r = 0;
    rep(i, n) {
        qq.push(a[3 * n - 1 - i]);
        sum_r += a[3 * n - 1 - i];
    }
    r[n] = sum_r;

    rep_s(i, 1, n + 1) {
        ll tmp = qq.top();
        qq.pop();
        if (tmp > a[3 * n - n - i]) {
            qq.push(a[3 * n - n - i]);
            sum_r -= tmp;
            sum_r += a[3 * n - n - i];
        } else {
            qq.push(tmp);
        }
        r[n - i] = sum_r;
    }
    ll ans = -INF;

    rep(i, n + 1) {
        ll tmp = l[i] - r[i];
        ans = max(ans, tmp);
    }
    cout << ans << "\n";
    return 0;
}