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
    vector<ll> q(n);
    for (ll i = 0; i < n; i++) cin >> q[i];

    vector<ll> r(n, 0);
    rep(i, n) r[i] = i + 1;
    ll a, b;
    ll i = 1;
    do {
        i++;
        if (r == p) a = i;
        if (r == q) b = i;
    } while (next_permutation(r.begin(), r.end()));

    cout << abs(a - b) << "\n";
    return 0;
}