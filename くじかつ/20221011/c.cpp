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
    map<ll, ll> ele;
    for (ll i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            n /= i;
            ele[i]++;
        }
    }
    if (n != 1) ele[n]++;

    ll ans = 0;
    rep_e(e, ele) {
        auto [key, val] = e;
        ll i = 0;
        while (1) {
            if ((i + 1) * (i + 2) / 2 <= val)
                i++;
            else
                break;
        }
        ans += i;
    }
    cout << ans << "\n";
    return 0;
}