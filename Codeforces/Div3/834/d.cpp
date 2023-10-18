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
// #define MOD 1000000007
#define MOD 998244353
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

ll pow_ll(ll n, ll p) {
    ll rest = 1;
    while (p) {
        if (p % 2 == 1) rest *= n;
        n *= n;
        p >>= 1;
    }
    return rest;
}

int main() {
    ll t;
    cin >> t;
    rep(_, t) {
        ll n, m;
        cin >> n >> m;
        ll two = 0, five = 0;
        ll now = n;
        while (now % 2 == 0) {
            two++;
            now /= 2;
        }
        while (now % 5 == 0) {
            five++;
            now /= 5;
        }
        ll ans = 0;
        ll num = n * m;
        for (ll i = 0; i < 30; i++) {
            for (ll j = 0; j < 13; j++) {
                if (pow_ll(2, i) * pow_ll(5, j) > m) continue;
                ll res = min(two + i, five + j);
                if (res > ans) {
                    ans = res;
                    ll div = m / pow_ll(2, i) / pow_ll(5, j);
                    num = n * div * pow_ll(2, i) * pow_ll(5, j);
                }
            }
        }

        cout << num << "\n";
    }

    return 0;
}