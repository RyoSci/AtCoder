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
    ll n, x, m;
    cin >> n >> x >> m;

    vector<ll> seen(m);
    vector<ll> sum(m);

    ll a = x;
    ll tot = 0;
    ll cycle_len = -1;
    ll cycle_sum = -1;
    ll start = -1;
    rep(i, n) {
        if (seen[a] != 0) {
            cycle_len = i + 1 - seen[a];
            cycle_sum = tot + a - sum[a];
            start = seen[a];
            break;
        }
        seen[a] = i + 1;
        tot += a;
        sum[a] = tot;
        a = (a % m) * (a % m);
        a %= m;
    }

    if (cycle_len == -1) {
        cout << tot << "\n";
    } else {
        ll tot = 0;
        ll a = x;
        rep(i, start - 1) {
            tot += a;
            a = (a % m) * (a % m);
            a %= m;
        }

        n -= start - 1;
        tot += cycle_sum * (n / cycle_len);
        rep(i, n % cycle_len) {
            tot += a;
            a = (a % m) * (a % m);
            a %= m;
        }
        cout << tot << "\n";
    }

    return 0;
}