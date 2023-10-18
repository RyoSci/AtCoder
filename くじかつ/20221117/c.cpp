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
    string s;
    cin >> s;
    set<ll> r, g, b;

    rep(i, n) {
        if (s[i] == 'R')
            r.insert(i);
        else if (s[i] == 'G')
            g.insert(i);
        else if (s[i] == 'B')
            b.insert(i);
    }

    ll ans = 0;
    rep_e(i, r) {
        rep_e(j, g) {
            ll ni = i;
            ll nj = j;
            if (ni > nj) swap(ni, nj);
            ll dis = nj - ni;
            ll minus = 0;
            if (dis % 2 == 0 and b.count(ni + dis / 2) > 0) minus++;
            if (b.count(ni - dis) > 0) minus++;
            if (b.count(nj + dis) > 0) minus++;
            ans += b.size() - minus;
        }
    }
    cout << ans << "\n";
    return 0;
}