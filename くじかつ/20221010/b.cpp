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
    ll n, m;
    cin >> n >> m;
    vector<ll> p(m);
    vector<string> s(m);
    for (ll i = 0; i < m; i++) cin >> p[i] >> s[i];

    vector<ll> acs(n, 0), was(n, 0);
    ll wa = 0;
    rep(i, m) {
        p[i]--;
        if (s[i] == "AC") {
            acs[p[i]]++;
            if (acs[p[i]] == 1) wa += was[p[i]];
        } else
            was[p[i]]++;
    }
    ll ac = 0;
    rep(i, n) if (acs[i] > 0) ac++;
    cout << ac << ' ' << wa << "\n";
    return 0;
}