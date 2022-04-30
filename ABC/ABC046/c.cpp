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
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define rep(i, n) for (ll i = 0; i < n; i++)
#define rep_r(i, k, n) for (ll i = k; i > n; i--)
#define rep_s(i, k, n) for (ll i = k; i < n; i++)
#define rep_e(e, s) for (auto e : s)

int main() {
    ll n;
    cin >> n;
    ll t = 1, a = 1;
    rep(i, n) {
        ll ti, ai;
        cin >> ti >> ai;
        // t以上のtiの倍数で最小
        ll nt = ((t - 1) / ti + 1) * ti;
        ll na = nt / ti * ai;
        // cout << nt << ' ' << na << "\n";
        if (a > na) {
            na = ((a - 1) / ai + 1) * ai;
            nt = na / ai * ti;
        }
        t = nt;
        a = na;

        // //
        // t,aに足すのをp,qとする。フェルマーの小定理と同じ原理でaiで割り切れるのp,qが存在する。
        // rep(q, 5001) {
        //     ll tmp = (a + q) * ti - t * ai;
        //     if (tmp % ai == 0) {
        //         ll p = tmp / ai;
        //         t = t + p;
        //         a = a + q;
        //         cout << i << " " << t << ' ' << a << "\n";
        //         break;
        //     }
        // }
    }
    cout << t + a << "\n";
    return 0;
}