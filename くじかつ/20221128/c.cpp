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
    ll n, w;
    cin >> n >> w;
    ll m = 200100;
    vector<ll> tot(m);
    rep(i, n) {
        ll s, t, p;
        cin >> s >> t >> p;
        tot[s] += p;
        tot[t] -= p;
    }
    rep(i, m - 1) tot[i + 1] += tot[i];

    bool ans = true;
    rep(i, m) if (tot[i] > w) ans = false;

    cout << (ans ? "Yes" : "No") << "\n";
    return 0;
}