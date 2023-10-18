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
    ll n, k;
    cin >> n >> k;
    vector<ll> p(n, 0);
    rep(i, n) {
        ll a, b, c;
        cin >> a >> b >> c;
        p[i] = a + b + c;
    }
    vector<ll> q(n, 0);
    q = p;
    sort(q.begin(), q.end());

    rep(i, n) {
        auto dis = upper_bound(q.begin(), q.end(), p[i] + 300) - q.begin();
        if (n - dis + 1 <= k)
            cout << "Yes"
                 << "\n";
        else
            cout << "No"
                 << "\n";
    }

    return 0;
}