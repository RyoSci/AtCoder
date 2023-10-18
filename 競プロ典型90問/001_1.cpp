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

ll n, l;
ll k;
vector<ll> a;

bool f(ll m) {
    ll cnt = 0;
    ll now = 0;
    while (now < l) {
        auto iter = lower_bound(a.begin(), a.end(), now + m);
        if (*iter == INF) break;
        now = *iter;
        cnt++;
    }
    return cnt > k;
}

int main() {
    cin >> n >> l;
    cin >> k;
    a.resize(n + 2);
    for (ll i = 0; i < n; i++) cin >> a[i];
    a[n] = l;
    a[n + 1] = INF;

    ll ok = 0;
    ll ng = l + 10;

    while (ok + 1 < ng) {
        ll m = (ok + ng) / 2;
        if (f(m))
            ok = m;
        else
            ng = m;
    }
    cout << ok << "\n";
    return 0;
}