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

ll n, k;
vector<int> a, b;

bool f(ll m) {
    ll cnt = 0;

    for (ll i = 0; i < n; i++) {
        ll ai = a[i];

        if (ai == 0) {
            if (0 < m) cnt += n;
        } else if (ai > 0) {
            ll aj;
            if (m >= 0)
                aj = (m + ai - 1) / ai;
            else
                aj = m / ai;
            ll tmp = lower_bound(a.begin(), a.end(), aj) - a.begin();
            cnt += tmp;
        } else {
            ai *= -1;
            ll aj;
            if (m >= 0)
                aj = (m + ai - 1) / ai;
            else
                aj = m / ai;
            ll tmp = lower_bound(b.begin(), b.end(), aj) - b.begin();
            cnt += tmp;
        }

        if (ai * ai < m) cnt -= 1;
    }

    return cnt / 2 < k;
}

int main() {
    cin >> n >> k;

    a.resize(n);
    for (ll i = 0; i < n; i++) cin >> a[i];

    sort(a.begin(), a.end());

    b.resize(n);
    for (ll i = n - 1; i >= 0; i--) b[n - 1 - i] = -a[i];

    ll ok = -INF;
    ll ng = INF;
    // ll ok = -10;
    // ll ng = 10;

    while (ok + 1 < ng) {
        ll m = (ok + ng) / 2;

        if (f(m))
            ok = m;
        else
            ng = m;
    }

    cout << ok << endl;

    return 0;
}
