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

ll n, c, d;
vector<ll> a;

bool f(ll m) {
    ll res = 0;
    // ll j = 0;
    // rep(i, d) {
    //     if (j % (m + 1) < n) {
    //         {
    //             res += a[j % (m + 1)];
    //             j++;
    //         }
    //     } else {
    //         i = (i + m) / (m + 1) * (m + 1);
    //         i--;
    //         j = 0;
    //     }
    // }
    rep(i, d) {
        if (i % (m + 1) < n) res += a[i % (m + 1)];
    }
    return c <= res;
}

int main() {
    ll t;
    cin >> t;
    rep(_, t) {
        cin >> n >> c >> d;
        a.resize(n);
        for (ll i = 0; i < n; i++) cin >> a[i];
        sort(a.rbegin(), a.rend());

        ll cnt = 0;

        if (a[0] * d < c)
            cout << "Impossible"
                 << "\n";
        else {
            ll ok = 0;
            ll ng = INF;

            while (ok + 1 < ng) {
                ll m = (ok + ng) / 2;
                if (f(m))
                    ok = m;
                else
                    ng = m;
            }
            if (ok == INF - 1)
                cout << "Infinity"
                     << "\n";
            else
                cout << ok << "\n";
        }
    }
    return 0;
}