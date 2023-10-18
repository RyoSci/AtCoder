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
    ll n = 100000 + 10;
    vector<ll> prime(n, 1);
    prime[0] = prime[1] = 0;
    rep_s(i, 2, n) {
        if (prime[i] == 0) continue;
        for (ll j = 2 * i; j < n; j += i) prime[j] = 0;
    }

    vector<ll> like2017(n, 0);
    rep(i, n) {
        if (i % 2 == 1 and prime[i] == 1 and prime[(i + 1) / 2] == 1)
            like2017[i] = 1;
    }

    rep(i, n - 1) like2017[i + 1] += like2017[i];

    ll q;
    cin >> q;
    rep(i, q) {
        ll l, r;
        cin >> l >> r;
        cout << like2017[r] - like2017[l - 1] << "\n";
    }

    return 0;
}