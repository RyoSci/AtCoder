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
    ll m = 1001001;
    vector<ll> tot(m, 0);
    rep(i, n) {
        ll l, r;
        cin >> l >> r;
        tot[l]++;
        tot[r]--;
    }
    rep(i, m - 1) tot[i + 1] += tot[i];

    rep(i, m - 1) {
        if (tot[i] == 0 and tot[i + 1] != 0) {
            cout << i + 1 << " ";
        }

        if (tot[i] != 0 and tot[i + 1] == 0) {
            cout << i + 1 << "\n";
        }
    }
    return 0;
}