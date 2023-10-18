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
    vector<ll> a;
    ll ans = 0;

    for (ll i = 1; i * i <= n; i++) {
        ans += n / i;
        a.push_back(n / i);
    }
    a.push_back(n / a[a.size() - 1]);

    reverse(a.begin(), a.end());

    rep(i, a.size() - 1) { ans += (a[i + 1] - a[i]) * (n / a[i + 1]); }

    cout << ans << "\n";
    // for (auto a : a) cout << a << " ";
    // cout << endl;
    return 0;
}