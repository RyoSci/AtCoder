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

    ll a;
    ll tot = 0;
    ll cycle_len = -1;
    ll cycle_sum = -1;
    ll start = -1;
    rep_s(i, 1, n + 1) {
        if (i == 1)
            a = x;
        else {
            a = (a % m) * (a % m);
            a %= m;
        }
        tot += a;

        if (seen[a] != 0) {
            cycle_len = i + 1 - seen[a];
            cycle_sum = tot - sum[a];
            start = seen[a];
            break;
        }
        seen[a] = i + 1;
        sum[a] = tot;
    }

    if (cycle_len == -1) {
        cout << tot << "\n";
    } else {
        ll a;
        ll tot = 0;
        rep_s(i, 1, start) {
            if (i == 1)
                a = x;
            else {
                a = (a % m) * (a % m);
                a %= m;
            }
            tot += a;
        }

        n -= start - 1;
        tot += cycle_sum * (n / cycle_len);
        rep(i, n % cycle_len) {
            a = (a % m) * (a % m);
            a %= m;
            tot += a;
        }
        cout << tot << "\n";
    }

    return 0;
}