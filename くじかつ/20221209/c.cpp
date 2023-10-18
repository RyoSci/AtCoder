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
    ll a, b, x;
    cin >> a >> b >> x;
    ll ok = 0, ng = 1000000001;

    auto f = [&](ll m) {
        ll res = a * m;
        while (m > 0) {
            res += b;
            m /= 10;
        }
        return res;
    };

    while (ok + 1 < ng) {
        ll m = (ok + ng) / 2;
        if (f(m) <= x)
            ok = m;
        else
            ng = m;
    }
    cout << ok << "\n";
    return 0;
}